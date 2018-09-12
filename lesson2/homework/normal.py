# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

from math import sqrt

origin_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []

print(origin_list)

for obj in origin_list:
    if obj >= 0 and obj%sqrt(obj) == 0:
            new_list.append(int(sqrt(obj)))
    else: 
        # print(f'{obj} не имеет квадратного корня или корень не целое число')
        pass
        
print(new_list)


print()
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

MONTHS = { 1: 'января',
           2: 'февраля',
           3: 'марта',
           4: 'апреля',
           5: 'мая',
           6: 'июня',
           7: 'июля',
           8: 'августа',
           9: 'сентября',
           10: 'октября',
           11: 'ноября',
           12: 'декабря'
}

DAYS = { 1: 'первое',
         2: 'второе',
         3: 'третье',
         4: 'четвертое',
         5: 'пятое',
         6: 'шестое',
         7: 'седьмое',
         8: 'воьсмое',
         9: 'девятое',
         10: 'десятое',
         11: 'одинадцатое',
         12: 'двенадцатое',
         13: 'тринадцатое',
         14: 'четырнадцатое',
         15: 'пятнадцатое',
         16: 'шестнадцатое',
         17: 'семьнадцатое',
         18: 'восемнадцатое',
         19: 'девятьнадцатое',
         20: 'двадцатое',
         21: 'двадцать первое',
         22: 'двадцать второе',
         23: 'двадцать третье',
         24: 'двадцать четвертое',
         25: 'двадцать пятое',
         26: 'двадцать шестое',
         27: 'двадцать седьмое',
         28: 'двадцать восьмое',
         29: 'двадцать девятое',
         30: 'тридцатое',
         31: 'тридцать первое'    
}

date = input('Введите дату в формате dd.mm.yyyy: ')

day = int(date.split('.')[0])
month = int(date.split('.')[1])
year = int(date.split('.')[2])

print(f'{DAYS[day]} {MONTHS[month]} {year} года')



print()
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

from random import randint

n = int(input('Введите количество элементов в списке: '))
new_list = []

for i in range(0,n):
    new_list.append(randint(-100, 100))

print(f'Ваш новый список: {new_list}')


print('')
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

origin_list = [1, 2, 4, 5, 6, 2, 5, 2]
print(f'Исходный список: {origin_list}')

list1 = list(set(origin_list))
list2 = []

for num in origin_list:
    if origin_list.count(num) > 1:
        continue
    else:
        list2.append(num)

print(f'Список из неповторяющихся элементов: {list1}')
print(f'Список элементов, у которых нет повторений: {list2}')
