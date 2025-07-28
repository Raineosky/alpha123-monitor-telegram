import requests
import hashlib
import time
import os

URL = "https://alpha123.uk/"
BOT_TOKEN = "8363909925:AAEWPGt2A0Dvs-1Xnp1FO1Te8tbh9rvQv7Y"
CHAT_ID = "6127595624"
LAST_HASH_FILE = "last_hash.txt"

def get_website_hash():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        content = response.text.encode("utf-8")
        return hashlib.sha256(content).hexdigest()
    except Exception as e:
        print("Error fetching website:", e)
        return None

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print("Error sending Telegram message:", e)

def load_last_hash():
    if not os.path.exists(LAST_HASH_FILE):
        return ""
    with open(LAST_HASH_FILE, "r") as f:
        return f.read().strip()

def save_last_hash(hash_value):
    with open(LAST_HASH_FILE, "w") as f:
        f.write(hash_value)

if __name__ == "__main__":
    new_hash = get_website_hash()
    if not new_hash:
        exit()

    last_hash = load_last_hash()
    if new_hash != last_hash:
        send_telegram_message("🔔 網站內容有變更！
" + URL)
        save_last_hash(new_hash)
    else:
        print("No change detected.")
