
"""

    TOP recommendation loader library implements a Spacy-based module to generate content recommendations using Natural Language Processing (NLP)  similarity techniques.

    It reads content from file sources such as CSV, JSON, and other supported formats to analyse and recommend related content based on similarity levels.

Author: Oghenetejiri Peace Onosajerhe.
 """


#imports#
from spacy import load

language_model = "en_core_web_lg"
nlp = load(language_model)


def load_contents(data, data_key: str, number_of_data: int = 10, nummber_of_content: int = 50):
    data_list = []

    for data_index in range(0, number_of_data):
        data_item = data[data_index][data_key]
        transformed_data = {data_key: data_item[:nummber_of_content]}
        data_list.append(transformed_data)

    return data_list


def tokenize_data(data):
    pass


def generate_recommendations(data, similarity_score: float=0.5, similar_recommendations=10, alternative_recommendations=5):
    pass

