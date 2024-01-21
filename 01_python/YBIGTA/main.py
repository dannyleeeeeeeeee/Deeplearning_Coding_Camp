import argparse
from YBIGTA.tokenizers import BPETokenizer, WordTokenizer
from YBIGTA.preprocessing import Preprocessor

def main():
    parser = argparse.ArgumentParser(description="Tokenizer CLI")
    parser.add_argument("--use_bpe", action="store_true", help="Use BPE tokenizer")
    parser.add_argument("--n_corpus", type=int, default=30000, help="Size of the corpus")
    parser.add_argument("--n_iter", type=int, default=10000, help="Number of iterations for training")
    args = parser.parse_args()
    
    corpus = ["Ybigta studies big data.", "I study data science."]

    preprocessor = Preprocessor()
    preprocessed_corpus = preprocessor.preprocess_corpus(corpus)

    if args.use_bpe:
        tokenizer = BPETokenizer(corpus=preprocessed_corpus)
    else:
        tokenizer = WordTokenizer()
        tokenizer.add_corpus(preprocessed_corpus)

    result = tokenizer.tokenize("Test tokenization.")

    print(result)

if __name__ == "__main__":
    main()

