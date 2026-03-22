
"""
    TOP Recommendation Loader Library

    This library implements a spaCy-based module to generate content recommendations using Natural Language Processing (NLP) similarity techniques.

    It reads content from file sources such as CSV, JSON, and other supported formats, analyzes them, and recommends related content based on similarity levels.

Author: Oghenetejiri Peace Onosajerhe.
 """


#imports#
from spacy import load
from spacy.cli import download
from spacy.tokens import Doc

language_model = "en_core_web_lg"

try:
    nlp = load(language_model)
except OSError:
    download(language_model)
    nlp = load(language_model)


def load_contents(
        data: list[dict[str, str]],
                  data_key: str,
                  number_of_data: int = 10,
                  number_of_content: int = 50
                  ):

    return [
        {data_key: data_item[data_key][:number_of_content]}
        for data_item in data[:number_of_data]
    ]


def tokenise_data(
        data: list[dict[str, str]],
                  data_key: str
                  ):
    
    text_data = [data_item[data_key] for data_item in data]
    docs = list(nlp.pipe(text_data))
    return [
        {data_key: doc}
        for doc in docs
    ]


def generate_recommendations(
        data: list[dict[str, Doc]],
        data_key: str,
        lookup_recommendation_value: Doc,
        similarity_score: float=0.5,
        number_of_recommendations=10
        ):
    
    similar_recommendations = []

    for data_item in data:
        doc = data_item[data_key]
        current_score = lookup_recommendation_value.similarity(doc)

        if current_score >= similarity_score:
            similar_recommendations.append((current_score, doc.text))

    similar_recommendations.sort(key=lambda d: d[0], reverse=True)
    top_recommendations = similar_recommendations[:number_of_recommendations]

    return [
        {data_key: content, "similarity_score": score}
        for score, content in top_recommendations
    ]


def generate_alternative_recommendations(
        data: list[dict[str, Doc]],
        data_key: str,
        lookup_recommendation_value: Doc,
        min_score: float=0.3,
        similarity_score: float=0.5,
        number_of_alternative_recommendations=10
        ):
    
    alternative_recommendations = []

    for data_item in data:
        doc = data_item[data_key]
        current_score = lookup_recommendation_value.similarity(doc)

        if min_score <= current_score <  similarity_score :
            alternative_recommendations.append((current_score, doc.text))

    alternative_recommendations.sort(key=lambda d: d[0], reverse=True)
    top_recommendations = alternative_recommendations[:number_of_alternative_recommendations]

    return [
        {data_key: content, "similarity_score": score}
        for score, content in top_recommendations
    ]
