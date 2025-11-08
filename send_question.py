import os
import random
import requests
from ielts_questions import questions

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# انتخاب تصادفی یک سوال
q = random.choice(questions)

# ساخت متن پیام
text = f"📚 IELTS B2 Question:\n\n{q['question']}\n\n"
for opt in q['options']:
    text += f"{opt}\n"

# دکمه شیشه‌ای برای نمایش پاسخ
reply_markup = {
    "inline_keyboard": [[{"text": "description", "callback_data": q['answer'] + "|" + q['explanation']}]]
}

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, json={"chat_id": CHAT_ID, "text": text, "reply_markup": reply_markup})
