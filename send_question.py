import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot

# دریافت توکن و چت آی‌دی از محیط
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# سوال‌ها، گزینه‌ها و توضیح پاسخ
questions = [
    {
        "question": "Which sentence is grammatically correct?",
        "options": ["She don’t like pizza.", "She doesn’t likes pizza.", "She doesn’t like pizza.", "She not like pizza."],
        "answer": 2,
        "explanation": "The correct form is 'She doesn’t like pizza.' because we use 'doesn’t' with base verb."
    },
    {
        "question": "Choose the correct word: I’m looking forward ___ your reply.",
        "options": ["for", "to", "at", "in"],
        "answer": 1,
        "explanation": "The correct phrase is 'looking forward to' which is followed by a noun or verb-ing."
    },
    {
        "question": "Select the correct sentence:",
        "options": ["If I will see him, I tell him.", "If I see him, I will tell him.", "If I saw him, I will tell him.", "If I see him, I tell him."],
        "answer": 1,
        "explanation": "The correct form for first conditional is 'If I see him, I will tell him.'"
    },
    {
        "question": "Which word is a synonym of 'happy'?",
        "options": ["Sad", "Joyful", "Angry", "Tired"],
        "answer": 1,
        "explanation": "'Joyful' is a synonym for 'happy'."
    },
    {
        "question": "Choose the correct passive form: 'They are building a new bridge.'",
        "options": ["A new bridge is built by them.", "A new bridge is being built by them.", "A new bridge built by them.", "A new bridge was built by them."],
        "answer": 1,
        "explanation": "Present continuous passive is 'is being built'."
    },
    {
        "question": "Pick the correct sentence:",
        "options": ["He suggested to go home.", "He suggested going home.", "He suggested go home.", "He suggested gone home."],
        "answer": 1,
        "explanation": "'Suggest' is followed by verb-ing, so 'He suggested going home.' is correct."
    },
    {
        "question": "Which sentence uses correct preposition?",
        "options": ["She is good in painting.", "She is good at painting.", "She is good on painting.", "She is good for painting."],
        "answer": 1,
        "explanation": "The correct preposition is 'good at'."
    },
    {
        "question": "Select the correct sentence:",
        "options": ["I have visited Paris last year.", "I visited Paris last year.", "I visit Paris last year.", "I have been visiting Paris last year."],
        "answer": 1,
        "explanation": "Past simple is used with a finished time: 'I visited Paris last year.'"
    },
    {
        "question": "Choose the correct word: I’m not used ___ getting up early.",
        "options": ["to", "for", "with", "at"],
        "answer": 0,
        "explanation": "'Be used to' is followed by noun or verb-ing, so 'used to getting up early' is correct."
    },
    {
        "question": "Which sentence is correct?",
        "options": ["There’s too much people here.", "There are too many people here.", "There is too many people here.", "There are too much people here."],
        "answer": 1,
        "explanation": "Use 'many' with countable nouns: 'too many people'."
    }
]

# انتخاب تصادفی یک سوال
question_data = random.choice(questions)

text = question_data["question"]

# ساخت دکمه‌ها
keyboard = [[InlineKeyboardButton(opt, callback_data=str(i))] for i, opt in enumerate(question_data["options"])]
keyboard.append([InlineKeyboardButton("Show Explanation", callback_data="show_explanation")])
reply_markup = InlineKeyboardMarkup(keyboard)

# ارسال پیام با دکمه‌ها
bot = Bot(TOKEN)
bot.send_message(chat_id=CHAT_ID, text=text, reply_markup=reply_markup)
