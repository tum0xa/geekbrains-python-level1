# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


origin_list = [1, 2, 4, 0]
new_list = [x**2 for x in origin_list]

print(origin_list)
print(new_list)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_1 = ['яблоко', 'банан', 'арбуз', 'киви', 'ананас']
fruit_list_2 = ['киви', 'груша', 'апельсин', 'арбуз', 'виноград', 'ананас']
fruit_list = [x for x in (set(fruit_list_1) & set(fruit_list_2))]
print(fruit_list_1)
print(fruit_list_2)
print(fruit_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4