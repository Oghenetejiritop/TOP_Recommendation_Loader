# TOP_Recommendation_Loader

A production-oriented Natural Language Processing (NLP) module for generating content recommendations using spaCy and semantic similarity techniques.

This project showcases efficient text preprocessing, scalable tokenization, and similarity-based ranking, demonstrating practical approaches to building recommendation systems using vector embeddings and NLP pipelines.

---

## Key Features

- **Data Ingestion**: Supports structured data inputs (Python dictionaries; extensible to CSV/JSON)
- **Preprocessing Controls**: Configurable dataset size and content truncation
- **High-Performance Tokenization**: Uses `spaCy`’s `nlp.pipe()` for efficient batch processing
- **Semantic Similarity Matching**: Leverages vector embeddings via `Doc.similarity()`
- **Tiered Recommendations**:
  - Primary Recommendations (high relevance)
  - Alternative Recommendations (moderate relevance)
- **Ranked Output**: Results sorted by similarity score for relevance-first retrieval

---

## System Overview

The pipeline follows a structured NLP workflow:

### 1. Content Loading
- Limits dataset size and text length for controlled processing

### 2. Tokenization
- Converts raw text into spaCy `Doc` objects with vector embeddings

### 3. Similarity Computation
- Computes semantic similarity between a query and dataset documents

### 4. Ranking & Filtering
- Applies threshold-based filtering
- Sorts results by similarity score (descending)

### 5. Recommendation Tiers
- **Primary**: score ≥ threshold (e.g., ≥ 0.5)
- **Alternative**: lower_bound ≤ score < threshold (e.g., 0.3–0.49)

---

## Tech Stack

- **Language**: Python 3.9+
- **NLP Framework**: spaCy (`en_core_web_lg`)

### Core Concepts
- Tokenization & pipelines
- Vector embeddings
- Semantic similarity (cosine similarity via spaCy)
- Data preprocessing & ranking algorithms

---

## Installation

### 1. Clone the Repository
git clone https://github.com/oghenetejiritop/top_recommendation_loader.git
cd top_recommendation_loader

### 2. Install Dependencies
pip install spacy
python -m spacy download en_core_web_lg
 
### Usage Example

from recommendation_loader import (
    load_contents,
    tokenise_data,
    generate_recommendations,
    generate_alternative_recommendations
)
import spacy

nlp = spacy.load("en_core_web_lg")

### Sample dataset
data = [
    {"content": "Artificial Intelligence is transforming industries."},
    {"content": "Machine learning is a subset of AI."},
    {"content": "Cooking recipes require ingredients and steps."}
]

### Step 1: Load content
loaded = load_contents(data, data_key="content")

### Step 2: Tokenize
tokenized = tokenise_data(loaded, data_key="content")

### Step 3: Define query
query = nlp("AI and machine learning")

### Step 4: Generate recommendations
main_results = generate_recommendations(tokenized, "content", query)
alt_results = generate_alternative_recommendations(tokenized, "content", query)

print("Primary Recommendations:")
for r in main_results:
    print(r)

print("\nAlternative Recommendations:")
for r in alt_results:
    print(r)
 

## Project Structure
top_recommendation_loader/
- top_recommendation_loader.py   # Core NLP and recommendation engine
- examples/                  # Example usage scripts
- README.md                  # Project documentation
- requirements.txt           # Dependencies
 
### Roadmap
* Add native CSV/JSON loaders
*Implement vector caching for large-scale datasets
*Build CLI interface for interactive querying
*Add unit and integration tests
*Optimize similarity computation using vectorized operations (NumPy)
 
### Example Output

Primary Recommendations:
{'content': 'Machine learning is a subset of AI.', 'similarity_score': 0.87}

Alternative Recommendations:
{'content': 'Artificial Intelligence is transforming industries.', 'similarity_score': 0.42}
 
 ## Author
 
Oghenetejiri Peace Onosajerhe
- [GitHub](https://github.com/oghenetejiritop)
- [LinkedIn](https://linkedin.com/in/oghenetejiritop) 

 ## License

 This project is licensed under the MIT License.

