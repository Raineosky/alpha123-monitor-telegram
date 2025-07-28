import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = "https://alpha123.uk/"
last_content = None

def fetch_page():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error: {e}"

def send_telegram_message(message):
    telegram_api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(telegram_api, data=payload)
    except Exception as e:
        print("Failed to send Telegram message:", e)

while True:
    current_content = fetch_page()
    global last_content
    if current_content != last_content and "Error" not in current_content:
        send_telegram_message("📢 網頁內容已變更： https://alpha123.uk/")
        last_content = current_content
    time.sleep(600)  # 每 10 分鐘檢查一次
