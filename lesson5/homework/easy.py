import os
import sys

def create_dir_by_path(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'{path} - директория/файл по данномму пути уже существует!')
    else:
        print(f'Директория {path} успешно создана.')


def delete_dir_by_path(path):
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print(f'{path} - директории по данному пути не существует!')
    else:
        print(f'Директория {path} успешно удалена.')


def print_list_dir_by_path(path):
    objects = os.listdir(path)
    print(f'Список директорий в папке {path}{os.path.sep}: ')
    for obj in objects:
        if os.path.isdir(obj):
            print(obj)


if __name__ == '__main__':

    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

    NUM_OF_DIRS = 10
    NAME_PREFIX = 'dir_'

    for i in range(NUM_OF_DIRS):
        dir_path = f'{NAME_PREFIX}{i}'
        create_dir_by_path(dir_path)

    input('Чтобы  продолжить нажмите "Enter".')

    for i in range(NUM_OF_DIRS):
        dir_path = f'{NAME_PREFIX}{i}'
        delete_dir_by_path(dir_path)

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    print_list_dir_by_path(os.getcwd())
    input('Чтобы  продолжить нажмите "Enter".')

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    cur_file_name = sys.argv[0]
    new_file_name = '_copy.'.join(cur_file_name.split('.'))

    with open(cur_file_name) as src:
        for line in src:
            with open(new_file_name, 'a') as dst:
                dst.write(line)
    if os.path.exists(new_file_name) and os.path.isfile(new_file_name):
        print(f'Файл {cur_file_name} успешно скопирован в {new_file_name}!')
    else:
        print('Не удалось скопировать файл!')

    input('Чтобы  продолжить нажмите "Enter".')
