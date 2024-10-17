"""
Этот файл содержит функцию для получения числа из изображения.
"""
from digitalgaz.config import NUMBER_MODEL

def get_number(image_path: str) -> str | None:
    """ 
    Функция возвращает число, если оно определено моделью, если на картинке числа нет - возвращает None.
    :param image_path: Путь к изображению
    :return : Значение с датчика или None
    """
    result = NUMBER_MODEL(image_path, conf=0.5)
    if result is None or len(result) == 0:
        return result
    preds = result[0].cpu().numpy() 
    sorted_data = sorted(preds.boxes.data, key=lambda number: (number[0], number[1]))
    predicted_digits = []  # Список для предсказанных цифр
    for el in sorted_data:
        predicted_digits.append(str(int(el[-1])))  # Добавляем цифру в список
    # Собираем предсказанные цифры в одну строку и преобразуем в число
    predicted_number = ''.join(predicted_digits)
    return predicted_number