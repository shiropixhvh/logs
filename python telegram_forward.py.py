<<<<<<< HEAD
from telethon import TelegramClient, events

# 🔹 ЗАМЕНИ НА СВОИ ДАННЫЕ (получи на my.telegram.org)
API_ID = 12559030  # Твой API ID
API_HASH = "d71f5869a2a857577663d5791fc6c9bb"  # Твой API Hash

# 🔹 ID получателя, которому пересылать сообщения
FORWARD_TO_ID = 950246781  # Заменить на реальный Telegram ID

# Создаем клиент
client = TelegramClient("my_session", API_ID, API_HASH)

@client.on(events.NewMessage(from_users="@team_visa_bot"))  # Заменить на username бота
async def forward_bot_messages(event):
    await client.send_message(FORWARD_TO_ID, f"📩 Сообщение от бота:\n\n{event.message.text}")

print("✅ Бот запущен и слушает сообщения...")
client.start()
client.run_until_disconnected()
=======
from telethon import TelegramClient, events

# 🔹 ЗАМЕНИ НА СВОИ ДАННЫЕ (получи на my.telegram.org)
API_ID = 12559030  # Твой API ID
API_HASH = "d71f5869a2a857577663d5791fc6c9bb"  # Твой API Hash

# 🔹 ID получателя, которому пересылать сообщения
FORWARD_TO_ID = 950246781  # Заменить на реальный Telegram ID

# Создаем клиент
client = TelegramClient("my_session", API_ID, API_HASH)

@client.on(events.NewMessage(from_users="@team_visa_bot"))  # Заменить на username бота
async def forward_bot_messages(event):
    await client.send_message(FORWARD_TO_ID, f"📩 Сообщение от бота:\n\n{event.message.text}")

print("✅ Бот запущен и слушает сообщения...")
client.start()
client.run_until_disconnected()
>>>>>>> 57d923d (first)
