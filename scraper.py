import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_titles():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []
    for item in soup.select(".titleline"):
        title_tag = item.find("a")
        if title_tag:
            titles.append({
                "title": title_tag.text,
                "link": title_tag["href"]
            })

    return titles

if __name__ == "__main__":
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "titles": scrape_titles()
    }

    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Scraping terminé. Résultats dans output.json")
