import time

from digitalgaz.cv import get_number, get_dimension


def process_image(file_path: str) -> dict:
    """
    Функция возвращает информацию о значении, размерности, типа измеряемого параметра и время обработки изображения
    :param file_path: путь к файлу
    :return: словарь с информацией о количестве и типе расхода
    """
    result = {}
    start_time = time.time()
    number = get_number(file_path)
    dimension = get_dimension(file_path)
    end_time = time.time()
    result["value"] = number if number else "Не определено"
    result["dimension"] = "m^3" if "m-3" in dimension else "-"
    result["type"] = "Расход" if "rashod" in dimension else "-"
    result["time"] = end_time - start_time
    return result