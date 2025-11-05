import os
import requests
import random

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# چند جمله نمونه انگلیسی (می‌تونی هر روز اضافه‌اش کنی)
sentences = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Don’t watch the clock; do what it does. Keep going.",
    "The best way to predict the future is to create it.",
    "Every day is a new beginning. Take a deep breath and start again."
]

sentence = random.choice(sentences)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={"chat_id": CHAT_ID, "text": sentence})
