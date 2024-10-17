import os
from typing import Any
from ultralytics import YOLO


def get_env(name: str) -> Any:
    """
    Функция возвращает значение переменной окружения с именем name
    Если значение не найдено, то выбрасывает исключение KeyError
    :param name: имя переменной окружения
    :return: значение переменной окружения
    """
    try:
        return os.environ[name]
    except KeyError:
        raise KeyError(f"{name} is not set in the environment")



IMG_PATH = get_env("IMG_PATH")
TOKEN = get_env("TOKEN")

NUMBER_MODEL = YOLO('bestofthebest.pt')
DIMENSION_MODEL = YOLO("best_andrey.pt")