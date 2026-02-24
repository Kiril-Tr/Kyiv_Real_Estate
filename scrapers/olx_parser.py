import requests
from bs4 import BeautifulSoup

def parse_olx():
    url = "https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            ads = soup.find_all('a', href=True)
            
            count = 0
            for ad in ads:
                title_element = ad.find('h6')
                
                if title_element:
                    title = title_element.text.strip()
                    link = ad['href']
                    
                    if link.startswith('/'):
                        link = "https://www.olx.ua" + link
                        
                    print(f"📌 {title}")
                    print(f"🔗 Посилання: {link}")
                    print("-" * 40)
                    
                    count += 1
                    if count == 5:
                        break
        else:
            print(f"Status: {response.status_code}")
            
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    parse_olx()