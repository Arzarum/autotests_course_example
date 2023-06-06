# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
from typing import TextIO

# Здесь пишем код

with open('test_file/task1_data.txt', 'r', encoding='utf-8') as task_data, \
     open(r'test_file/task1_answer.txt', mode='w', encoding='utf-8') as test_file:
    for i in task_data.readlines():
        test_file.write(''.join([letter for letter in i if not letter.isdigit()]))


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
