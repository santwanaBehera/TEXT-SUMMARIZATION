# utils/text_summarizer.py

from .summarizer_utils import extractive_summary, abstractive_summary

class TextSummarizer:
    @staticmethod
    def summarize(text, method="extractive", sentences_count=3, max_length=120):
        if method == "extractive":
            return extractive_summary(text, sentence_count=sentences_count)
        elif method == "abstractive":
            return abstractive_summary(text, max_length=max_length)
        elif method == "hybrid":
            extract = extractive_summary(text, sentence_count=sentences_count)
            return abstractive_summary(extract, max_length=max_length)
        else:
            raise ValueError(f"Invalid method: {method}")
