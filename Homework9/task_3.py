# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

sum_list = []
stor = 0
with open('test_file/task_3.txt', 'r') as task:
    for index, i in enumerate(task.readlines()):
        if not i == '\n':
            stor += int(i)
        else:
            sum_list.append(stor)
            stor = 0

three_most_expensive_purchases = sum(sorted(sum_list)[-3:])

assert three_most_expensive_purchases == 202346
print(three_most_expensive_purchases)