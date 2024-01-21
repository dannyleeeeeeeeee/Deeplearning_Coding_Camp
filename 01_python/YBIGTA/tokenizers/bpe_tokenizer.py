#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
from typing import Optional, Union, List

class BPETokenizer:
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        self.corpus = [] if corpus is None else self._preprocess_corpus(corpus)
        self.vocab = set()

    def add_corpus(self, corpus: Union[List[str], str]) -> None:
        new_data = self._preprocess_corpus(corpus)
        self.corpus.extend(new_data)

    def train(self, n_iter: int) -> None:
        for _ in range(n_iter):
            pass

    def tokenize(self, text: Union[List[str], str], padding: bool = False, max_length: Optional[int] = None) -> Union[List[List[int]], List[int]]:
        pass

    def __call__(self, text, padding, max_length) -> Union[List[List[int]], List[int]]:
        return self.tokenize(text, padding, max_length)

    def _preprocess_corpus(self, corpus: Union[List[str], str]) -> List[str]:
        preprocessed_corpus = []
        if isinstance(corpus, str):
            preprocessed_corpus.append(self._preprocess_text(corpus))
        elif isinstance(corpus, list):
            preprocessed_corpus = [self._preprocess_text(text) for text in corpus]

        return preprocessed_corpus

    def _preprocess_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

if __name__ == "__main__":
    tokenizer = BPETokenizer(["This is a sample sentence.", "Another example sentence."])
    tokenizer.train(n_iter=1000)
    result = tokenizer.tokenize("Test tokenization.")
    print(result)

