import os
import requests

# Telegram configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_notification(message):
    # url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    # data = {"chat_id": CHAT_ID, "text": message}
    # response = requests.post(url, data=data)
    # return response.json()
    pass