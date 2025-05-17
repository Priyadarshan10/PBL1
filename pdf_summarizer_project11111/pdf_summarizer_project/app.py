import sys
import os
import tempfile
import streamlit as st

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import your utility functions
from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text, split_into_sentences
from utils.summarizer import load_keywords, get_top_sentences

# Streamlit page settings
st.set_page_config(page_title="PDF Summarizer", layout="centered")

st.title("📄 PDF Summarizer")
st.write("Upload a PDF and a keywords file to generate a summary.")

# Upload PDF file
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

# Upload keywords.txt file
keywords_file = st.file_uploader("Upload keywords.txt", type=["txt"])

# When "Generate Summary" is clicked
if st.button("Generate Summary") and pdf_file and keywords_file:
    # Save uploaded files to temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        tmp_pdf.write(pdf_file.read())
        tmp_pdf_path = tmp_pdf.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp_keywords:
        tmp_keywords.write(keywords_file.read())
        tmp_keywords_path = tmp_keywords.name

    # Run the summarization pipeline
    raw_text = extract_text_from_pdf(tmp_pdf_path)
    cleaned_text = clean_text(raw_text)
    sentences = split_into_sentences(cleaned_text)
    keywords = load_keywords(tmp_keywords_path)
    summary = get_top_sentences(sentences, keywords)

    # Display the summary
    if summary:
        st.success("✅ Summary Generated:")
        for i, line in enumerate(summary, 1):
            st.write(f"{i}. {line.strip()}")

        # Enable download
        full_summary = "\n".join(f"- {line.strip()}" for line in summary)
        st.download_button("Download Summary", full_summary, file_name="summary.txt")
    else:
        st.warning("⚠️ No relevant sentences found with the given keywords.")
