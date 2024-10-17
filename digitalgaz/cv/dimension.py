"""
Этот файл содержит для определения размерностей значений
"""
from digitalgaz.config import DIMENSION_MODEL


def get_dimension(path: str) -> list[str | None]:
    """
    Функция для определения размерностей и определения расход или не расход
    :param path: Путь к изображению
    :return : массив с данными:
    m-3 - размерность кубический метр
    rashod - значит мы связаны с расходом
    пустой массив - модель не смогла ничего определить
    """
    # Запуск модели для изображения
    results = DIMENSION_MODEL(path, show=False, conf=0.4, save=False)

    # Проверяем первый результат
    result = results[0]  # получаем первый элемент из списка

    # Получаем информацию о предсказанных объектах
    boxes = result.boxes  # информация о найденных объектах

    # Если есть обнаруженные объекты
    if boxes is not None and len(boxes) > 0:
        detected_classes = [result.names[int(box.cls)] for box in boxes]  # список классов объектов
    else:
        detected_classes = []

    return detected_classes
