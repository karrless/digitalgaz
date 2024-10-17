import asyncio

import uvicorn
from dotenv import load_dotenv
load_dotenv()

def web_start():
  uvicorn.run("digitalgaz.app:app", host="karrless.ru", port=3005, reload=True)

async def bot_run():
    from digitalgaz.bot import bot, dp
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot started")
    await dp.start_polling(bot)

def bot_start():
    asyncio.run(bot_run())

asyncio.run(bot_run())