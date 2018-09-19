# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys

import easy


print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print('rm <file_name> - удаляет указанный файл ')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy():
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None
        print('Не указано имя файла для копирования!')
    else:
        easy.copy_file_by_path(file_name)


def remove():
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None
        print('Не указано имя файла для удаления!')
    else:
        easy.delete_file_by_path(file_name)


def change_dir():
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None
        print('Не указань путь для смены текущей директории!')
    else:
        print('Текущая директория:', os.getcwd())
        if easy.change_cur_dir_by_path(dir_name):
            print('Директория сменена на:', os.getcwd())
        else:
            print('Не удалось сменить директорию!')


def show_full_path():
    print('Текущий путь:')
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy,
    "rm": remove,
    "cd": change_dir,
    "ls": show_full_path,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
