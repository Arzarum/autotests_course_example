# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("data, result", [
    ((4, 2), 2),
    pytest.param((60, 3, 5), 4, marks=pytest.mark.smoke),
    pytest.param((6.6, 2), 3.3, marks=pytest.mark.skip)],
                         ids=["test_int", "test_mult_int", "test_float"])
def test_all(data, result):
    total = all_division(*numbers)
    assert total == expected_result

