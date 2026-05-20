import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

SEED_URLS = [
    "https://www.menlo.edu/",
    "https://www.menlo.edu/academics/",
    "https://www.menlo.edu/student-life/",
    "https://www.menlo.edu/admissions/",
]

OUT = Path("data/menlo_pages.json")

def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def fetch_page(url: str) -> dict:
    html = requests.get(url, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    title = clean(soup.get_text(" ")[:120])
    text = clean(soup.get_text(" "))
    return {"url": url, "title": title, "text": text[:6000]}

def main():
    pages = []
    seen = set()

    for url in SEED_URLS:
        try:
            page = fetch_page(url)
            pages.append(page)
            seen.add(url)
        except Exception as e:
            print(f"Skip {url}: {e}")

    OUT.write_text(json.dumps(pages, indent=2))
    print(f"Wrote {len(pages)} pages to {OUT}")

if __name__ == "__main__":
    main()
