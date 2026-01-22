
"""

    TOP recommendation loader library implements a Spacy-based module to generate content recommendations using Natural Language Processing (NLP)  similarity techniques.

    It reads content from file sources such as CSV, JSON, and other supported formats to analyse and recommend related content based on similarity levels.

Author: Oghenetejiri Peace Onosajerhe.
 """


#imports#
from spacy import load

language_model = "en_core_web_lg"
nlp = load(language_model)


def load_contents(data, num_data: int = 10):
    pass


def tokenize_data(data):
    pass


