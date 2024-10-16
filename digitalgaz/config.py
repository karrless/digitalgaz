import os
from typing import Any

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