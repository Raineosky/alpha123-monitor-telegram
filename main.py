
import os
import time
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = "https://alpha123.uk/"

last_content = ""

def fetch_website():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(telegram_url, data=data)

def main():
    global last_content
    while True:
        try:
            content = fetch_website()
            if content != last_content:
                send_telegram_message("網站內容已更新！")
                last_content = content
        except Exception as e:
            send_telegram_message(f"監控錯誤：{e}")
        time.sleep(600)  # 每 10 分鐘檢查一次

if __name__ == "__main__":
    main()
