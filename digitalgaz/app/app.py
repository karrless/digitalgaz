"""
Этот файл содержит приложение, которое обрабатывает пост запросы с фотографией датчика.
"""
from fastapi import FastAPI, File, HTTPException, UploadFile
import aiofiles as aiof

from digitalgaz.config import IMG_PATH
from digitalgaz.cv import process_image

app = FastAPI()

@app.post("/api")
async def get_flow_value(file: UploadFile = File(...)) -> dict[str, str]:
    """
    Обработка пост запроса с фотографией датчика. Возвращает значение датчика и время обработки фотографии.
    :param file: файл с фотографией датчика
    :return: значение датчика и время обработки фотографии
    :raises HTTPException: если файл не является изображением
    """
    # Проверка типа файла на соответствие
    if not file.content_type.startswith('image'):
        # Если файл не является изображением, выбрасываем исключение
        raise HTTPException(status_code=400, detail="File is not a valid image.")
    
    # Создание пути к файлу
    file_path = IMG_PATH+file.filename
    
    # Сохранение файла в папку IMG_PATH
    async with aiof.open(file_path, mode='wb') as f:
        content = await file.read()
        await f.write(content)

    info = process_image(file_path)

    return info

@app.get("/api")
async def index() -> dict[str, str]:
    """
    Обработка GET запроса
    :return: сообщение "Hello from ООСД!"
    """
    return {"message":"Hello from ООСД!"}
