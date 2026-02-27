import requests
from bs4 import BeautifulSoup

def get_domria_data():
    url = "https://dom.ria.com/uk/arenda-kvartir/kiev/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    results = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            ads = soup.find_all('a', href=True)
            for ad in ads:
                link = ad['href']
                if '/uk/realty' in link or '/uk/neruhomist' in link:
                    title = ad.text.strip()
                    if title and len(title) > 5:
                        full_link = "https://dom.ria.com" + link if link.startswith('/') else link
                        results.append({"title": title, "link": full_link})
                        if len(results) == 5: break
        return results
    except:
        return []

if __name__ == "__main__":
    data = get_domria_data()
    for item in data:
        print(f"📌 {item['title']}\n🔗 {item['link']}\n")