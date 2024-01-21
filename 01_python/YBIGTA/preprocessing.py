import re
from typing import List

class Preprocessor:
    def __init__(self):
        pass

    def preprocess_corpus(self, corpus: List[str]) -> List[str]:
        return [self._preprocess_text(text) for text in corpus]

    def _preprocess_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

if __name__ == "__main__":
    corpus = ["Ybigta studies big data.", "I study data science."]
    
    preprocessor = Preprocessor()
    preprocessed_corpus = preprocessor.preprocess_corpus(corpus)
    print(preprocessed_corpus)

