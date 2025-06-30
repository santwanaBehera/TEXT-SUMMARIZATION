from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from transformers import pipeline
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Final Spacy-compatible tokenizer for Sumy
class SpacyTokenizer:
    def __init__(self, language="english"):
        self.language = language

    def to_sentences(self, text):
        doc = nlp(text)
        return [str(sent).strip() for sent in doc.sents]

    def to_words(self, sentence):
        doc = nlp(sentence)
        return [token.text for token in doc if not token.is_space]

# Extractive summarization using spaCy + TextRank
def extractive_summary(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, SpacyTokenizer())
    summarizer = TextRankSummarizer()
    summary_sentences = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary_sentences)

# Abstractive summarization using HuggingFace Transformers
def abstractive_summary(text, min_length=30, max_length=120):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]['summary_text']
