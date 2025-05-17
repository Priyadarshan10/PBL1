
def load_keywords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]

def score_sentence(sentence, keywords):
    return sum(word in sentence.lower() for word in keywords)

def get_top_sentences(sentences, keywords, top_n=5):
    scored = [(s, score_sentence(s, keywords)) for s in sentences]
    scored = sorted(scored, key=lambda x: x[1], reverse=True)
    return [s for s, score in scored[:top_n] if score > 0]
