# app/summarizer.py

from transformers import pipeline

# Abstractive summarizer using Hugging Face
summarizer = pipeline("summarization")

def abstractive_summary(text):
    return summarizer(text, max_length=120, min_length=30, do_sample=False)[0]['summary_text']

# Extractive summarizer using Sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def extractive_summary(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count=3)
    return " ".join(str(sentence) for sentence in summary)
