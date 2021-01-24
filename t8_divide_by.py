"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Нужно отредактировать функцию is_divide_by, которая принимает 3 аргумента:

- to_divide - число для проверки
- divider_1 - первый делитель
- divider_2 - второй делитель

таким образом, чтобы она возвращала True, если число для проверки делится
без остатка на 2 делителя, и False, если нет

ПРИМЕРЫ
--------------------------------------------------------------------------------
- is_divide_by(-12, 2, -6)  ->  True
- is_divide_by(45, 5, 15)   ->  True ### ОШИБКА ДОЛЖНО БЫТЬ 45, 3, 15
- is_divide_by(4, 1, 4)     ->  True
- is_divide_by(15, -5, 3)   ->  True
- is_divide_by(-12, 2, -5)  ->  False
- is_divide_by(45, 1, 6)    ->  False
"""


def is_divide_by(to_divide: int, divider_1: int, divider_2: int) -> bool:
    """Проверяет делится ли нацело to_divide нацело на divider_1 и divider_2

    :param to_divide: число для проверки
    :type to_divide: int

    :param divider_1: первый делитель
    :type divider_1: int

    :param divider_2: второй делитель
    :type divider_2: int

    :return: True, если делится на 2 числа, False, если нет
    :rtype: bool
    """
    if to_divide%divider_1==0 and to_divide%divider_2==0 :
        return True
    else:
        return False


if __name__ == '__main__':
    to_divide = int(input('Введите число для проверки: '))
    divider_1 = int(input('Введите первый делитель: '))
    divider_2 = int(input('Введите второй делитель: '))
    print(f'{is_divide_by(to_divide, divider_1, divider_2)}')
