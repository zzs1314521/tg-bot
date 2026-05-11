import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    text = """
🎁 <b>欢迎进入福利领取通道</b>

当前可领取：
✅ 隐藏内容
✅ 限时福利
✅ 私密入口

完成赞赏后上传截图即可领取。
"""

    await message.answer(text)

@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer("✅ 已收到截图，请等待审核。")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())