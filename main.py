from telethon.sync import TelegramClient
import asyncio

API_ID = 24410919
API_HASH = "11a3a20ee4f9e851e35412b0a2eedb3a"

SESSION_NAME = "my_account"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def keep_online():
    await client.start()
    print("✅ Shaxsiy akkaunt onlayn!")

    while True:
        await client.send_message('me', '🟢 Online!')  # Har 5 daqiqada o‘zingizga xabar yuboradi
        await asyncio.sleep(300)

if __name__ == "__main__":
    client.loop.run_until_complete(keep_online())