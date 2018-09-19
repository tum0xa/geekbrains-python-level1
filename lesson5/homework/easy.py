# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os


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
    # if os.getcwd() == path:
    print(f'Список директорий в папке {path}{os.path.sep}: ')
    for obj in objects:
        if os.path.isdir(obj):
            print(obj)


if __name__ == '__main__':

    NUM_OF_DIRS = 10
    NAME_PREFIX = 'dir_'

    for i in range(NUM_OF_DIRS):
        dir_path = f'{NAME_PREFIX}{i}'
        create_dir_by_path(dir_path)

    input('Чтобы  продолжить нажмите любую кнопку.')

    for i in range(NUM_OF_DIRS):
        dir_path = f'{NAME_PREFIX}{i}'
        delete_dir_by_path(dir_path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

    print_list_dir_by_path(os.getcwd())
    input('Чтобы  продолжить нажмите любую кнопку.')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

