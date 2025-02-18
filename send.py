import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@conscious_child'

def job(parent, child):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "developer", "content": child },
            { "role": "user", "content": parent },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

daughter = f"Ты - осознанная дочь, у тебя большая обида на мать за ошибки, совершённые в детстве, но ты хочешь восстановить хорошие отношения"
mother = f"Пожелай хорошего дня матери, используй смайлики"

#job(mother, daughter)

schedule.every().day.at("07:00",'Europe/Moscow').do(job, parent=mother, child=daughter)

fifteen_minutes = 15 * 60

for i in range(fifteen_minutes):
    schedule.run_pending()
    time.sleep(1)
