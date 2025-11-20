import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

# 将来 DB に接続するときに使用
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

def fetch_suumo_count():
    url = "https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=020&ta=14&sc=14206"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    # 件数を抽出
    # Suumo よく変わるため、なるべく汎用的に取得
    count_elem = soup.select_one(".pagination_set-hit")
    if not count_elem:
        print("件数が取得できませんでした。HTML構造が変わっている可能性があります。")
        return

    count_text = count_elem.get_text(strip=True)
    print("Suumo 新築戸建て（神奈川県小田原市）の件数:", count_text)


if __name__ == "__main__":
    fetch_suumo_count()
