from typing import List, Union

class WordTokenizer:
    def tokenize(self, text: Union[List[str], str], padding: bool = False, max_length: int = None) -> List[str]:
        if isinstance(text, str):
            tokens = text.split()
        elif isinstance(text, list):
            tokens = [sentence.split() for sentence in text]
        else:
            raise ValueError("Input should be a string or a list of strings.")

        if max_length is not None:
            tokens = [sentence[:max_length] for sentence in tokens]

        if padding:
            max_sentence_length = max(len(sentence) for sentence in tokens)
            tokens = [sentence + ['[PAD]'] * (max_sentence_length - len(sentence)) for sentence in tokens]

        return tokens
