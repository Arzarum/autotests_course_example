# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime

# Здесь пишем код


def func_log(file_log='log.txt'):
    def decorator_func_log(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
            log_message = f"{func.__name__} вызвана {timestamp}\n"

            with open(file_log, mode='a+', encoding='utf-8') as log_file:
                log_file.write(log_message)

            return func(*args, **kwargs)

        return wrapper

    return decorator_func_log


@func_log()
def func1():
    pass


@func_log('func2.txt')
def func2():
    pass


func1()
func2()
func1()