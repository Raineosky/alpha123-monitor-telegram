import requests
import time
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://alpha123.uk/"
CHECK_INTERVAL = 600  # 10 分鐘

last_content = ""

def get_page_content():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        return f"Error: {e}"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
    }
    requests.post(url, data=data)

while True:
    global last_content
    content = get_page_content()

    if content != last_content:
        send_telegram_message("網站內容有變化！")
        last_content = content

    time.sleep(CHECK_INTERVAL)
