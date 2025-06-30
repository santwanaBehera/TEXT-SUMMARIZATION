# app.py

import streamlit as st
from utils.text_summarizer import TextSummarizer

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Text Summarizer App")
st.markdown("Summarize large texts using **Extractive**, **Abstractive**, or **Hybrid** methods.")

# Text input
text_input = st.text_area("Enter your text here 👇", height=300)

# File upload option
uploaded_file = st.file_uploader("Or upload a .txt file", type=["txt"])
if uploaded_file:
    text_input = uploaded_file.read().decode("utf-8")

# Select method
method = st.selectbox("Choose method", ["extractive", "abstractive", "hybrid"])
sentences = st.slider("Sentences (for extractive/hybrid)", 1, 10, 3)
max_length = st.slider("Max summary length (abstractive/hybrid)", 50, 300, 120)

# Run summarizer
if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter or upload text.")
    else:
        with st.spinner("Summarizing..."):
            try:
                summary = TextSummarizer.summarize(
                    text_input,
                    method=method,
                    sentences_count=sentences,
                    max_length=max_length
                )
                st.success("Here's your summary:")
                st.text_area("Summary", value=summary, height=200)
            except Exception as e:
                st.error(f"Error: {str(e)}")
