import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/"

headers = {"User-Agent": "Mozilla/5.0"} 
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


headline_tags = soup.find_all("h3")

headlines = []
for tag in headline_tags:
    text = tag.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)
    if len(headlines) >= 10: 
        break

with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, h in enumerate(headlines, 1):
        f.write(f"{i}. {h}\n")

print(f"Saved {len(headlines)} headlines to headlines.txt")