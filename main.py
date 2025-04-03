from telethon.sync import TelegramClient
import asyncio

# API ID va API HASH ma'lumotlarini o'zingizga moslab qo'ying
api_id = 24410919  # O'zingizning API ID-ni yozing
api_hash = '11a3a20ee4f9e851e35412b0a2eedb3a'  # O'zingizning API HASH-ni yozing
phone_number = '+998500175636'  # O'zingizning telefon raqamingizni yozing

# Session nomini to'g'ri kiriting (faylni yuklagan nom)
session_name = 'session_name'  # Faylingiz nomini kiriting

# TelegramClient yaratish
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start(phone_number)
    print("✅ Session faylidan foydalanish boshlandi.")
    
    # Telegram akkauntini doimiy onlayn holatda ushlab turish
    while True:
        await client.send_message('me', 'Online')  # Har 60 sekundda o'zingizga xabar yuboriladi
        await asyncio.sleep(60)  # 60 sekund kutadi

if __name__ == "__main__":
    import asyncio
    client.loop.run_until_complete(main())