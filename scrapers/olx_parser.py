import requests

def check_olx_connection():
    url = "https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Status: {response.status_code}")
            print("OLX Connection: OK")
        else:
            print(f"Status: {response.status_code}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_olx_connection()