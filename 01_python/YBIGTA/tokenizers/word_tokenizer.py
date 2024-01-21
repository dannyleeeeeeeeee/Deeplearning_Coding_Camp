#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
from typing import List, Optional

class WordTokenizer:
    def __init__(self):
        self.corpus = []
        self.vocab = set()

    def add_corpus(self, corpus: List[str]) -> None:
        self.corpus.extend(corpus)

    def tokenize(self, text: str, padding: bool = False, max_length: Optional[int] = None) -> List[int]:
        tokens = self._preprocess_text(text).split()
        token_ids = [self._get_or_add_token_id(token) for token in tokens]

        if padding and max_length:
            token_ids = token_ids[:max_length]
            token_ids += [0] * (max_length - len

