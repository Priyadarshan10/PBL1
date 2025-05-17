
from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text, split_into_sentences
from utils.summarizer import load_keywords, get_top_sentences

# File paths
pdf_file = '../input/sample.pdf'
keywords_file = '../input/keywords.txt'
output_file = '../output/summary.txt'

# Run the summarizer pipeline
raw_text = extract_text_from_pdf(pdf_file)
cleaned_text = clean_text(raw_text)
sentences = split_into_sentences(cleaned_text)
keywords = load_keywords(keywords_file)
summary = get_top_sentences(sentences, keywords)

# Write to file
with open(output_file, 'w', encoding='utf-8') as f:
    for line in summary:
        f.write(f"- {line.strip()}\n")



print("✅ Summary generated at:", output_file)
