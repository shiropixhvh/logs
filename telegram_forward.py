from telethon import TelegramClient, events
from flask import Flask
import os

# 🔹 ЗАМЕНИ НА СВОИ ДАННЫЕ (получи на my.telegram.org)
API_ID = 12559030  # Твой API ID
API_HASH = "d71f5869a2a857577663d5791fc6c9bb"  # Твой API Hash

# 🔹 ID получателя, которому пересылать сообщения
FORWARD_TO_ID = 950246781  # Заменить на реальный Telegram ID

# Создаем клиент Telethon
client = TelegramClient("my_session", API_ID, API_HASH)

# Flask приложение
app = Flask(__name__)

@app.route('/')
def home():
    return "Телеграм-бот работает!"

@client.on(events.NewMessage(from_users="@team_visa_bot"))  # Заменить на username бота
async def forward_bot_messages(event):
    await client.send_message(FORWARD_TO_ID, f"📩 Сообщение от бота:\n\n{event.message.text}")

print("✅ Бот запущен и слушает сообщения...")
client.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Получаем порт из переменной окружения
    app.run(host="0.0.0.0", port=port)  # Запускаем Flask сервер на нужном порту

