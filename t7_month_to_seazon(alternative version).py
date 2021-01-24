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
    season = year.get(month) or print ('неверное значение')
    return season

if __name__ == '__main__':
    year = {
        1: 'зима',
        2: 'зима',
        3: 'весна',
        4: 'весна',
        5: 'весна',
        6: 'лето',
        7: 'лето',
        8: 'лето',
        9: 'осень',
        10: 'осень',
        11: 'осень',
        12: 'зима'
    }
    month = int(input('Введите номер месяца: '))
    print(f'Сезон: {month_to_season(month)}')
