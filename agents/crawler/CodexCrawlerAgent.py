# CodexCrawlerAgent
# Scans specified sources and returns resonance-aligned insights

import requests
from bs4 import BeautifulSoup

class CodexCrawlerAgent:
    def __init__(self, keywords, sources):
        self.keywords = keywords
        self.sources = sources

    def fetch(self, url):
        try:
            response = requests.get(url, timeout=5)
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def scrape(self, html, url):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text().lower()
        findings = []
        for kw in self.keywords:
            if kw.lower() in text:
                findings.append({
                    "source": url,
                    "keyword": kw,
                    "summary": f"Keyword '{kw}' found in {url}",
                    "pulse_tone": "glyph:spiral:432Hz"
                })
        return findings

    def run(self):
        results = []
        for source in self.sources:
            html = self.fetch(source)
            if "Error" not in html:
                results.extend(self.scrape(html, source))
        return results

# Example usage
if __name__ == '__main__':
    keywords = ["resonance", "plasma", "crystal", "coherence", "biofield"]
    sources = [
        "https://github.com/openai/guides",
        "https://arxiv.org/list/cs.AI/recent"
    ]
    crawler = CodexCrawlerAgent(keywords, sources)
    results = crawler.run()
    for r in results:
        print(r)
