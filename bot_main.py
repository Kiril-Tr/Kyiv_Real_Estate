import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from scrapers.domria_parser import get_domria_data
from scrapers.database import init_db, is_new_ad

TOKEN = "8449814729:AAH0YjdK6DzdXWRLv7C90icEWQyJOIB8TPo"
from aiogram.client.default import DefaultBotProperties
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="Markdown"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("🔎 Шукаю нові квартири для тебе...")
    flats = get_domria_data()

    new_found = 0
    if flats:
        for flat in flats:
            if is_new_ad(flat['link']):
                text = f"✅ **НОВА КВАРТИРА!**\n\n📌 {flat['title']}\n🔗 {flat['link']}"
                await message.answer(text, parse_mode="Markdown")
                new_found += 1

        if new_found == 0:
            await message.answer("📭 Поки що нових оголошень немає.")
    else:
        await message.answer("❌ Щось пішло не так з пошуком.")

async def main():
    init_db()
    print("🤖 Бот запущений! Напиши /start у Телеграмі.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())