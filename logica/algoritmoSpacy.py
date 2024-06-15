import pandas as pd
from colorama import Fore, Style, init
from tabulate import tabulate
from logica.configIdioma import Language, LanguageConfig
import os

# Inicializar colorama
init(autoreset=True)

# Inicializar los DataFrames globales
df_es = pd.DataFrame()
df_en = pd.DataFrame()


class CoursePair:
    def __init__(self, local_name, local_syllabus, foreign_name, foreign_syllabus,
                 porcRealSimilarity, lang=Language.SPANISH):
        self.local_name = local_name
        self.local_syllabus = local_syllabus
        self.foreign_name = foreign_name
        self.foreign_syllabus = foreign_syllabus
        self.porcRealSimilarity = porcRealSimilarity
        self.lang = lang
        self.nlp = LanguageConfig.get_model(lang)
        self.stop_words = LanguageConfig.get_stop_words(lang)
        self.cleaned_localName = self.clean_text(local_name)
        self.cleaned_localSyllabus = self.clean_text(local_syllabus)
        self.cleaned_foreignName = self.clean_text(foreign_name)
        self.cleaned_foreignSyllabus = self.clean_text(foreign_syllabus)

    def clean_text(self, text):
        doc = self.nlp(text)
        tokens = [token.lemma_.lower() for token in doc if token.is_alpha and token.text.lower() not in self.stop_words]
        return ' '.join(tokens)


class SimilarityCalculator:
    def __init__(self, course_pair):
        self.nlp = course_pair.nlp
        self.cleaned_localName = course_pair.cleaned_localName
        self.cleaned_localSyllabus = course_pair.cleaned_localSyllabus
        self.cleaned_foreignName = course_pair.cleaned_foreignName
        self.cleaned_foreignSyllabus = course_pair.cleaned_foreignSyllabus
        self.porcRealSimilarity = course_pair.porcRealSimilarity
        self.TOTAL_SIMILARITY = self.calculate_similarity()
        self.convalidable = self.calculate_Convalidable()
        self.efficiency = self.calculate_efficiency()

    def calculate_efficiency(self):
        efficiency = (100 - abs(self.porcRealSimilarity - self.TOTAL_SIMILARITY))
        return efficiency

    def get_name_syllabus_similarity(self):
        docLocalName = self.nlp(self.cleaned_localName)
        docLocalSyllabus = self.nlp(self.cleaned_localSyllabus)
        docForeignName = self.nlp(self.cleaned_foreignName)
        docForeignSyllabus = self.nlp(self.cleaned_foreignSyllabus)
        namesSimilarity = (docLocalName.similarity(docForeignName))
        syllabusSimilarity = (docLocalSyllabus.similarity(docForeignSyllabus))

        return namesSimilarity, syllabusSimilarity

    def calculate_similarity(self):
        namesSimilarity, syllabusSimilarity = self.get_name_syllabus_similarity()

        umbral = 0

        if namesSimilarity < 0.1:
            umbral = 0.35
        elif namesSimilarity < 0.2:
            umbral = 0.30
        elif namesSimilarity < 0.3:
            umbral = 0.25
        elif namesSimilarity < 0.4:
            umbral = 0.20
        elif namesSimilarity < 0.5:
            umbral = 0.15
        elif namesSimilarity < 0.6:
            umbral = -0.03
        elif namesSimilarity < 0.7:
            umbral = -0.05
        elif namesSimilarity < 0.8:
            umbral = -0.10

        TOTAL_SIMILARITY = syllabusSimilarity - umbral

        return TOTAL_SIMILARITY * 100

    def calculate_Convalidable(self):
        return "NO" if self.TOTAL_SIMILARITY < 75 else "SÍ"


order_Num_ES = 0
order_Num_EN = 0
table_es = []
table_en = []


class ConvalidationTable:
    order_Num_es = order_Num_ES
    order_Num_en = order_Num_EN

    def __init__(self, course_pair, courseSimilarity_obj):
        self.local_name = course_pair.local_name
        self.local_syllabus = course_pair.local_syllabus
        self.foreign_name = course_pair.foreign_name
        self.foreign_syllabus = course_pair.foreign_syllabus
        self.porcRealSimilarity = course_pair.porcRealSimilarity
        self.similarity = courseSimilarity_obj.TOTAL_SIMILARITY
        self.convalidable = courseSimilarity_obj.convalidable
        self.efficiency = courseSimilarity_obj.efficiency
        self.lang = course_pair.lang

        # Agregar los datos al DataFrame
        df = self.add_to_dataframe()
        if self.lang == Language.SPANISH:
            global df_es
            df_es = pd.concat([df_es, df], ignore_index=True)
        elif self.lang == Language.ENGLISH:
            global df_en
            df_en = pd.concat([df_en, df], ignore_index=True)

    def getTableOrderNum(self):
        table = []
        orderNum = 0

        if self.lang == Language.SPANISH:
            ConvalidationTable.order_Num_es += 1
            orderNum = ConvalidationTable.order_Num_es
            table = table_es
        elif self.lang == Language.ENGLISH:
            ConvalidationTable.order_Num_en += 1
            orderNum = ConvalidationTable.order_Num_en
            table = table_en
        return table, orderNum

    def add_result_to_table(self):
        color = Fore.GREEN if self.convalidable == "SÍ" else Fore.RED
        convalidable_colored = color + self.convalidable + Style.RESET_ALL
        table, orderNum = self.getTableOrderNum()
        table.append([orderNum, self.local_name, self.local_syllabus, self.foreign_name, self.foreign_syllabus,
                      self.porcRealSimilarity, f"{self.similarity:.2f}%", convalidable_colored, self.efficiency])

    @staticmethod
    def blue_headers(headers):
        return [Fore.BLUE + header + Style.RESET_ALL for header in headers]

    def display(self):
        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        datasetDirectory = os.path.join(parent_directory, "documentos/datasetNLP.csv")

        if self.lang == Language.SPANISH:
            headers = ["#", "Curso Local", "Sumilla Local", "Curso Postulante", "Sumilla Postulante", "Simil. Real (%)",
                       "Simil. Calculada (%)", "Convalidable", "Eficiencia (%)"]
            print(tabulate(table_es, headers=self.blue_headers(headers), tablefmt="fancy_grid"))
            df_es.to_csv(datasetDirectory, index=False)
        elif self.lang == Language.ENGLISH:
            headers = ["#", "Curso Local", "Sumilla Local", "Curso Postulante", "Sumilla Postulante", "Simil. Real (%)",
                       "Simil. Calculada (%)", "Convalidable", "Eficiencia (%)"]
            print(tabulate(table_en, headers=self.blue_headers(headers), tablefmt="fancy_grid"))
            df_en.to_csv(datasetDirectory, index=False)

    def add_to_dataframe(self):
        table, orderNum = self.getTableOrderNum()
        data = {
            "#": orderNum,
            "Curso Local": self.local_name,
            "Sumilla Local": self.local_syllabus,
            "Curso Postulante": self.foreign_name,
            "Sumilla Postulante": self.foreign_syllabus,
            "Simil. Real (%)": self.porcRealSimilarity,
            "Simil. Calculada (%)": f"{self.similarity:.2f}%",
            "Convalidable": self.convalidable,
            "Eficiencia (%)": self.efficiency
        }
        df = pd.DataFrame(data, index=[0])
        return df
