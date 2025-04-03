import os
from telethon.sync import TelegramClient
import asyncio

# Muhit o‘zgaruvchilaridan API ID, API HASH va telefon raqamini olish
api_id = int(os.getenv("API_ID", 24410919))
api_hash = os.getenv("API_HASH", "11a3a20ee4f9e851e35412b0a2eedb3a")
phone_number = os.getenv("PHONE_NUMBER", "+998945975009")
session_name = os.getenv("SESSION_NAME", "session_name")  # Fayl nomi

# TelegramClient yaratish
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start(phone_number)
    print("✅ Session faylidan foydalanish boshlandi.")

    while True:
        await client.send_message('me', 'Online')
        await asyncio.sleep(60)  # 60 sekund kutadi

if __name__ == "__main__":
    client.loop.run_until_complete(main())
