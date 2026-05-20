import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PAGES_PATH = Path("data/menlo_pages.json")

def search_menlo_website(query: str, top_k: int = 3) -> str:
    if not PAGES_PATH.exists():
        return "Website index missing. Run: python app/ingest_website.py"

    pages = json.loads(PAGES_PATH.read_text())
    docs = [p["text"] for p in pages]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]

    chunks = ["MENLO WEBSITE SEARCH RESULTS:"]
    for idx, score in ranked:
        p = pages[idx]
        excerpt = p["text"][:1200]
        chunks.append(f"\nTitle: {p['title']}\nURL: {p['url']}\nScore: {score:.3f}\nExcerpt: {excerpt}")

    return "\n".join(chunks)
