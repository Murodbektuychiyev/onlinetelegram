import asyncio
from telethon import TelegramClient

# Session fayli nomi (avval yaratganingiz)
SESSION_NAME = "session_name"

# API ID va API HASH kiritilmaydi, chunki `.session` faylidan olinadi
client = TelegramClient(SESSION_NAME, api_id=None, api_hash=None)

async def main():
    await client.start()  # Avtomatik sessionni yuklash
    print("✅ Shaxsiy akkaunt Render'da onlayn bo‘ldi.")

    while True:
        await client.send_message("me", "✅ Hali ham onlaynman!")  # Har 30 daqiqada o'zingizga xabar yuboriladi
        await asyncio.sleep(1800)  # 30 daqiqa kutish

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())