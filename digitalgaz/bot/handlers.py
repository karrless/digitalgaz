from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from digitalgaz.bot import bot
from digitalgaz.config import IMG_PATH
from digitalgaz.cv import process_image

router = Router()

@router.message(Command("start"))
async def start_command_handler(msg: Message):
    """
    Обработчик команды '/start'
    :param msg: сообщение
    :return:
    """
    await msg.answer(text='Добро пожаловать в бот ООСД!\nПришлите изображение датчика (обязательно документом!)')


@router.message(F.document)
async def get_image(msg: Message):
    """
    Обработчик сообщения с документом
    :param msg: сообщение
    """
    doc = msg.document
    if not doc.mime_type.startswith('image'):
        # Если файл не является изображением, выбрасываем исключение
        return await msg.answer("Файл не является изображением, повторите попытку")
    await msg.answer("Обработка изображения...")
    file = await bot.get_file(doc.file_id)
    filename= IMG_PATH + file.file_unique_id + "." + doc.mime_type.split('/')[1]
    await bot.download_file(file.file_path, filename)
    info = process_image(filename)
    text = (f'Значение: {info.get("value")}\n'
            f'Размерность: {info.get("dimension")}\n'
            f'Тип: {info.get("type")}\n\n'
            f'Время на обработку: {info.get("time")} секунд')
    return await msg.answer(text=text)


@router.message()
async def get_image(msg: Message):
    """
    Обработчик сообщения без документа
    :param msg: сообщение
    """
    return await msg.answer(text="Это не документ, повторите попытку")