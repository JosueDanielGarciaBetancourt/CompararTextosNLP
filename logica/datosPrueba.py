import pandas as pd
import os


def returnCSVDataFrameEsp():
    try:
        # Obtener la ruta del archivo actual
        current_directory = os.path.dirname(__file__) if __file__ else os.getcwd()
        parent_directory = os.path.dirname(current_directory)

        datasetDirectory = os.path.join(parent_directory, "documentos/datasetCursosCSV.csv")

        df = pd.read_csv(datasetDirectory, encoding='UTF-8', delimiter=';', decimal='.')

        # Seleccionar los campos deseados
        fields = ['Nombre Curso Local', 'Silabo Curso Local', 'Nombre Curso Postulante',
                  'Silabo Curso Postulante', 'Porcentaje de Similitud']
        data = df[fields]

        # Renombrar las columnas para que sean más claras
        data.columns = ['nombreLocal', 'silaboLocal', 'nombrePostulante', 'silaboPostulante', 'porcRealSimilarity']

        # Imprimir solamente el contenido del CSV sin los headers
        # dataFrame = data.to_string(index=False, header=False)
        # print(dataFrame)

        return data
    except FileNotFoundError:
        print(f"El archivo en la ruta {datasetDirectory} no fue encontrado.")
    except pd.errors.EmptyDataError:
        print("El archivo CSV está vacío.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


class CoursesData:

    def __init__(self):
        self.cursos_locales = []
        self.cursos_postulantes = []

    @staticmethod
    def returnCursosEsp():
        """
        cursos_espanol = [
            {
                "nombreLocal": "Fundamentos de Programación",
                "silaboLocal": "Fundamentos de programación: algoritmos, estructuras de control, funciones y arreglos",
                "nombrePostulante": "Introducción a la Programación",
                "silaboPostulante": "Introducción a la Programación: uso de pseint, conceptos generales de programación",
                "porcRealSimilarity": 80,
            },
            {
                "nombreLocal": "Sistemas Operativos",
                "silaboLocal": "Sistemas operativos: gestión de procesos, memoria y dispositivos.",
                "nombrePostulante": "Medio ambiente",
                "silaboPostulante": "Abordaremos sobre el medio ambiente y el cuidado del planeta.",
                "porcRealSimilarity": 5,
            },
            {
                "nombreLocal": "Diseño de Interfaces de Usuario",
                "silaboLocal": "Principios de diseño de interfaces de usuario y experiencia de usuario (UI/UX).",
                "nombrePostulante": "Desarrollo Web Avanzado",
                "silaboPostulante": "Este curso cubre temas avanzados de desarrollo web, incluyendo frameworks modernos"
                                    " y diseño de interfaces interactivas.",
                "porcRealSimilarity": 70,
            },
            {
                "nombreLocal": "Bases de Datos Relacionales",
                "silaboLocal": "Fundamentos de bases de datos relacionales, modelado de datos y SQL.",
                "nombrePostulante": "Big data y ciencia de datos",
                "silaboPostulante": "Introducción a la ciencia de datos, big data y análisis predictivo "
                                    "utilizando herramientas modernas.",
                "porcRealSimilarity": 65,
            },
            {
                "nombreLocal": "Biología Celular",
                "silaboLocal": "Estudio de la estructura, función y comportamiento de las células.",
                "nombrePostulante": "Historia del arte",
                "silaboPostulante": "Exploración de las obras y movimientos artísticos a lo largo de la historia.",
                "porcRealSimilarity": 5,
            },
            {
                "nombreLocal": "Economía Internacional",
                "silaboLocal": "Análisis de las interacciones económicas entre diferentes países.",
                "nombrePostulante": "Cocina creativa",
                "silaboPostulante": "Curso práctico de cocina con enfoque en la creatividad culinaria.",
                "porcRealSimilarity": 5,
            },
            {
                "nombreLocal": "Matemáticas Discretas",
                "silaboLocal": "Teoría de conjuntos, lógica matemática, álgebra de Boole, relaciones y funciones.",
                "nombrePostulante": "Matemáticas Aplicadas",
                "silaboPostulante": "Aplicación de las matemáticas en la resolución de problemas del mundo real.",
                "porcRealSimilarity": 30,
            },
            {
                "nombreLocal": "Introducción a la Ingeniería de Sistemas",
                "silaboLocal": "Conceptos fundamentales de la ingeniería de sistemas, sistemas de información y tecnologías de la información.",
                "nombrePostulante": "Fundamentos de Ingeniería Industrial",
                "silaboPostulante": "Introducción a los principios básicos de la ingeniería industrial y "
                                    "su aplicación en diferentes industrias.",
                "porcRealSimilarity": 30,
            },
            {
                "nombreLocal": "Redes de Computadoras",
                "silaboLocal": "Principios básicos de las redes de computadoras, protocolos de comunicación y tecnologías de redes.",
                "nombrePostulante": "Seguridad Informática",
                "silaboPostulante": "Protección de la información y sistemas informáticos contra amenazas y ataques cibernéticos.",
                "porcRealSimilarity": 60,
            },
            {
                "nombreLocal": "Inteligencia Artificial",
                "silaboLocal": "Introducción a la inteligencia artificial, algoritmos de búsqueda, aprendizaje automático y redes neuronales.",
                "nombrePostulante": "Robótica Avanzada",
                "silaboPostulante": "Desarrollo de sistemas robóticos avanzados con enfoque en la inteligencia "
                                    "artificial y la interacción humano-robot.",
                "porcRealSimilarity": 75,
            }
        ]
        """

        cursos_espanol = []
        data = returnCSVDataFrameEsp()
        for index, row in data.iterrows():
            curso = {
                "nombreLocal": row['nombreLocal'],
                "silaboLocal": row['silaboLocal'],
                "nombrePostulante": row['nombrePostulante'],
                "silaboPostulante": row['silaboPostulante'],
                "porcRealSimilarity": row['porcRealSimilarity']
            }
            cursos_espanol.append(curso)

        return cursos_espanol

    @staticmethod
    def returnCursosEng():
        courses_english = [
            {
                "nombreLocal": "Programming Fundamentals",
                "silaboLocal": "Programming fundamentals: algorithms, control structures, functions, and arrays.",
                "nombrePostulante": "Introduction to Programming",
                "silaboPostulante": "Introduction to Programming: use of pseudocode, general programming concepts."
            },
            {
                "nombreLocal": "Operating Systems",
                "silaboLocal": "Operating systems: process management, memory, and devices.",
                "nombrePostulante": "Environmental Science",
                "silaboPostulante": "Study of the environment and planet conservation."
            },
            {
                "nombreLocal": "User Interface Design",
                "silaboLocal": "Principles of user interface and user experience design (UI/UX).",
                "nombrePostulante": "Advanced Web Development",
                "silaboPostulante": "This course covers advanced topics in web development, including modern frameworks and interactive interface design."
            },
            {
                "nombreLocal": "Relational Databases",
                "silaboLocal": "Fundamentals of relational databases, data modeling, and SQL.",
                "nombrePostulante": "Big Data and Data Science",
                "silaboPostulante": "Introduction to data science, big data, and predictive analysis using modern tools."
            },
            {
                "nombreLocal": "Cell Biology",
                "silaboLocal": "Study of the structure, function, and behavior of cells.",
                "nombrePostulante": "Art History",
                "silaboPostulante": "Exploration of artworks and artistic movements throughout history."
            },
            {
                "nombreLocal": "International Economics",
                "silaboLocal": "Analysis of economic interactions among different countries.",
                "nombrePostulante": "Creative Cooking",
                "silaboPostulante": "Practical cooking course with a focus on culinary creativity."
            },
            {
                "nombreLocal": "Discrete Mathematics",
                "silaboLocal": "Set theory, mathematical logic, Boolean algebra, relations, and functions.",
                "nombrePostulante": "Applied Mathematics",
                "silaboPostulante": "Application of mathematics in solving real-world problems."
            },
            {
                "nombreLocal": "Introduction to Systems Engineering",
                "silaboLocal": "Fundamental concepts of systems engineering, information systems, and information technologies.",
                "nombrePostulante": "Foundations of Industrial Engineering",
                "silaboPostulante": "Introduction to basic principles of industrial engineering and their application in different industries."
            },
            {
                "nombreLocal": "Computer Networks",
                "silaboLocal": "Basic principles of computer networks, communication protocols, and network technologies.",
                "nombrePostulante": "Information Security",
                "silaboPostulante": "Protection of information and computer systems against cyber threats and attacks."
            },
            {
                "nombreLocal": "Artificial Intelligence",
                "silaboLocal": "Introduction to artificial intelligence, search algorithms, machine learning, and neural networks.",
                "nombrePostulante": "Advanced Robotics",
                "silaboPostulante": "Development of advanced robotic systems with a focus on artificial intelligence and human-robot interaction."
            }
        ]

        return courses_english
