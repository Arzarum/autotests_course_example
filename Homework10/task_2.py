# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_zero_1():
    result = all_division(0, 66)
    assert result == 0


@pytest.mark.smoke
def test_zero_2():
    with pytest.raises(ZeroDivisionError):
        all_division(4, 0)


def test_int():
    result = all_division(4, 2)
    assert result == 2


def test_mult_int():
    result = all_division(60, 3, 5)
    assert result == 4


def test_float():
    result = all_division(6.6, 2)
    assert result == 3.3
