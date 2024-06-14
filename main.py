print("Hola, a continuación simularemos convalidaciones de algunos cursos."
      "\nRecuerda que un curso se convalida si supera el 75% de similitud."
      "\nEl proceso está iniciando, esto puede tardar de 10s a 30 seg...")

from logica.configIdioma import LanguageConfig
from logica.datosPrueba import CoursesData
from logica.algoritmoSpacy import CoursePair, SimilarityCalculator, ConvalidationTable


class ConvalidacionCursosUC:
    @staticmethod
    def convalidarCursos(dicCursos, lang):
        for curso in dicCursos:
            nombre_local = curso["nombreLocal"]
            silabo_local = curso["silaboLocal"]
            nombre_postulante = curso["nombrePostulante"]
            silabo_postulante = curso["silaboPostulante"]
            porcRealSimilarity = curso["porcRealSimilarity"]

            coursePair_obj = CoursePair(nombre_local, silabo_local, nombre_postulante, silabo_postulante,
                                        porcRealSimilarity, lang)
            courseSimilarity_obj = SimilarityCalculator(coursePair_obj)
            convalidation_table = ConvalidationTable(coursePair_obj, courseSimilarity_obj)
            convalidation_table.add_result_to_table()

        # Imprimir tabla con los resultados
        convalidation_table.display()

    @staticmethod
    def convalidarCursosEsp():
        dicCursosEsp = CoursesData.returnCursosEsp()
        ConvalidacionCursosUC.convalidarCursos(dicCursosEsp, LanguageConfig.returnSpanishLang())

    @staticmethod
    def convalidarCursosEng():
        dicCursosEng = CoursesData.returnCursosEng()
        ConvalidacionCursosUC.convalidarCursos(dicCursosEng, LanguageConfig.returnEnglishLang())


if __name__ == "__main__":
    print("\nCursos en español")
    # Simular convalidación de cursos en español
    ConvalidacionCursosUC.convalidarCursosEsp()
    #print("\n\nCursos en inglés")
    # Simular convalidación de cursos en inglés
    #ConvalidacionCursosUC.convalidarCursosEng()
    #print("\n")
