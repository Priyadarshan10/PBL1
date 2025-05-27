
import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_sentences(text):
    return sent_tokenize(text)
