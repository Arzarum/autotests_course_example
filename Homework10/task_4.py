# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time
import pytest


@pytest.mark.usefixtures('print_start_and_finish_tests')
class TestMyClass:

    def test_number_one(self):
        time.sleep(0.5)

    def test_number_two(self, print_test_timings):
        time.sleep(1)

    def test_number_three(self):
        time.sleep(1.5)
