import os
import telegram
import schedule
import time
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = telegram.Bot(token=BOT_TOKEN)

polls = [
    {
        "question": "2, 6, 12, 20, ?",
        "options": ["28", "30", "24", "26"],
        "correct": 0
    },
    {
        "question": "If A > B and B > C, then A > C?",
        "options": ["True", "False"],
        "correct": 0
    },
    {
        "question": "Which is a prime number?",
        "options": ["9", "15", "17", "21"],
        "correct": 2
    }
]

def send_poll():
    poll = random.choice(polls)
    bot.send_poll(
        chat_id=CHAT_ID,
        question=poll["question"],
        options=poll["options"],
        type="quiz",
        correct_option_id=poll["correct"],
        is_anonymous=False
    )

schedule.every(5).minutes.do(send_poll)

print("✅ Telegram poll bot running...")

while True:
    schedule.run_pending()
    time.sleep(1)

