from enum import Enum
import spacy
from spacy.lang.es.stop_words import STOP_WORDS as STOP_WORDS_ES
from spacy.lang.en.stop_words import STOP_WORDS as STOP_WORDS_EN


class Language(Enum):
    SPANISH = 'es'
    ENGLISH = 'en'


class LanguageConfig:
    STOP_WORDS = {
        Language.SPANISH: STOP_WORDS_ES.union({
            "de", "a", "el", "la", "las", "y", "en", "los", "del", "que", "con", "por", "para",
            "se", "su", "al", "como", "lo", "es", "más", "o", "u", "una", "uno", "le", "les",
            "me", "mi", "mí", "nos", "nosotros", "vosotros", "su", "sus", "nuestro", "nuestra",
            "nuestros", "nuestras", "vuestra", "vuestro", "vuestras", "vuestros", "ser", "fue",
            "soy", "eres", "son", "era", "fui", "fuiste", "fueron", "ese", "esa", "esos", "esas",
            "este", "esta", "estos", "estas", "."
        }),
        Language.ENGLISH: STOP_WORDS_EN.union({
            "of", "to", "the", "and", "in", "that", "it", "is", "was", "for", "on", "are", "as",
            "with", "his", "they", "at", "be", "this", "have", "from", "or", "one", "had", "by",
            "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there",
            "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other",
            "about", "out", "many", "then", "them", "these", "so", "some", "her", "would", "make",
            "like", "him", "into", "has", "look", "two", "more", "write", "go", "see", "number",
            "no", "way", "could", "people", "my", "than", "first", "water", "been", "call", "who",
            "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part", "."
        })
    }

    MODELS = {
        Language.SPANISH: spacy.load('es_core_news_lg'),
        Language.ENGLISH: spacy.load('en_core_web_lg')
    }

    @staticmethod
    def returnSpanishLang():
        return Language.SPANISH

    @staticmethod
    def returnEnglishLang():
        return Language.ENGLISH

    @staticmethod
    def get_stop_words(language):
        return LanguageConfig.STOP_WORDS[language]

    @staticmethod
    def get_model(language):
        return LanguageConfig.MODELS[language]

