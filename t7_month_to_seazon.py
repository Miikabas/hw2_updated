"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию month_to_season, которая принимает номер месяца,
таким образом, чтобы она возвращала название сезона, к которому относится
этот месяц

ПРИМЕРЫ
--------------------------------------------------------------------------------
- month_to_season(12) -> 'зима'
- month_to_season(4) -> 'весна'
- month_to_season(7) -> 'лето'
- month_to_season(9) -> 'осень'
"""


def month_to_season(month: int) -> str:
    """Возвращает сезон по его номеру

    :param month: номер сезона
    :type month: int

    :return: название сезона, например "зима"
    :rtype: str
    """

    if month == 1 or month == 2 or month == 12:
        result = "Зима"
    elif 3 <= month <= 5:
        result = "Весна"
    elif 6 <= month <= 8:
        result = "Лето"
    elif 9 <= month <= 11:
        result = "Осень"
    return result


if __name__ == '__main__':
    month = int(input('Введите номер месяца: '))
    f'{month_to_season(month)}'
