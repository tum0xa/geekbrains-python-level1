# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


def apply_tax(salary, tax):
    """
    Расчет зарплаты с учетом налога

    :param salary: Зарплата в рублях
    :param tax: Налог в %
    :return: Зарплата с учетом налога
    """
    return salary-salary*tax/100


def handler(line):
    """
    Обработчик строки из ведомости

    :param line: строка из ведомости
    :return: кортеж (ИМЯ_СОТРУДНИКА, Зарплата_в_рублях)
    """
    person, _, salary = line.split(' ')
    return person.upper(), int(salary)


def create_sheet(filename, persons, salaries):
    """
    Создание ведомости и её запись в файл

    :param filename: Имя файла ведомости
    :param persons: Список сотрудников
    :param salaries: Список зарплат сотрудников
    :return: Ничего не возращается
    """
    staff = dict(zip(persons, salaries))

    with open(filename, 'w') as sheet:
        for person in staff:
            salary = staff.get(person)
            if salary < 500000:  # Зарплаты более 500000 рублей не включаются в ведомость
                sheet.write(f'{person} - {salary}\n')


def read_sheet(filename):
    """
    Чтение ведомости из файла и вывод её на экран
    (зарплаты выводятся с учетом налога 13%)

    :param filename: Имя файла ведомости
    :return: Ничего не возращается
    """
    with open(filename, 'r') as sheet:
        for line in sheet:
            person, salary = handler(line)
            print(f'{person} - {apply_tax(salary,13)}')


persons = ['Алексей', 'Андрей', 'Мария', 'Игорь', 'Галина']
salaries = [5000, 100000, 50000, 500000, 32768]

create_sheet('sheet.csv', persons, salaries)

read_sheet('sheet.csv')




