
"""

    TOP recommendation loader library implements a SpaCy-based module to generate content recommendations using Natural Language Processing (NLP)  similarity techniques.

    It reads content from file sources such as CSV, JSON, and other supported formats to analyse and recommend related content based on similarity levels.

Author: Oghenetejiri Peace Onosajerhe.
 """


#imports#
from spacy import load

language_model = "en_core_web_lg"
nlp = load(language_model)


def load_contents(data: list[dict[str, str]], data_key: str, number_of_data: int = 10, number_of_content: int = 50):

    return [
        {data_key: data_item[data_key][:number_of_content]}
        for data_item in data[:number_of_data]
    ]


def tokenise_data(data: list[dict[str, str]], data_key: str):
    text_data = [data_item[data_key] for data_item in data]
    docs = list(nlp.pipe(text_data))
    return [
        {data_key: doc}
        for doc in docs
    ]


def generate_recommendations(data, similarity_score: float=0.5, similar_recommendations=10, alternative_recommendations=5):
    pass

