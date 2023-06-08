import pytest
from datetime import datetime


@pytest.fixture(scope='class')
def print_start_and_finish_tests():
    print('Время старта класса -', datetime.now().strftime('%H:%M:%S'))
    yield
    print('\nВремя окончания класса -', datetime.now().strftime('%H:%M:%S'))


@pytest.fixture()
def print_test_timings():
    start = datetime.now()
    print('\nВремя старта теста -', start.strftime('%H:%M:%S:%f'))
    yield
    finish = datetime.now()
    print('\nВремя финиша теста -', finish.strftime('%H:%M:%S:%f'))
    print('Время Выполнения теста -', (finish - start))