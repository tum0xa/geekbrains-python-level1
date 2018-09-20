import os
import sys


def create_dir_by_path(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'{path} - директория/файл по данномму пути уже существует!')
    else:
        print(f'Директория {path} успешно создана.')
    print()


def delete_dir_by_path(path):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        print(f'{path} - директории по данному пути не существует!')
    else:
        print(f'Директория {path} успешно удалена.')
    print()


def print_list_dir_by_path(path, only_dir=False):
    objects = os.listdir(path)
    print('Список', 'директорий' if only_dir else 'элементов', f'в папке {path}{os.path.sep}:\n')
    if objects:
        for obj in objects:
            if only_dir and os.path.isdir(obj):
                print(obj)
            else:
                print(obj)
    else:
        print('Текущая папка пустая!')
    print()


def change_cur_dir_by_path(path):
    if os.path.exists(path) and not os.path.isfile(path):
        os.chdir(os.path.normpath(path))
        return True
    else:
        print('Указанной папки не существует!')
        print()
        return False


def copy_file_by_path(path):
    new_file_name = '_copy.'.join(path.split('.'))

    with open(path) as src:
        with open(new_file_name, 'w') as dst:
            dst.writelines(src.readlines())
    if os.path.exists(new_file_name) and os.path.isfile(new_file_name):
        print(f'Файл {path} успешно скопирован в {new_file_name}!')
    else:
        print('Не удалось скопировать файл! Неизвестная ошибка!')


def delete_file_by_path(path):
    path = os.path.normpath(path)
    if os.path.exists(path) and os.path.isfile(path):
        if os.name == 'nt':
            os.system(f'del {path}')
        elif os.name == 'posix':
            os.system(f'rm {path}')
        else:
            print('Данная операция не поддерживается в вашей операционной системе!')
    else:
        print(f'{path} - файла не существует!')
    if not os.path.exists(path):
        print(f'{path} - файл успешно удалён!')
    print()


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

    print_list_dir_by_path(os.getcwd(), only_dir=True)
    input('Чтобы  продолжить нажмите "Enter".')

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    cur_file_name = sys.argv[0]
    copy_file_by_path(cur_file_name)

    input('Чтобы  продолжить нажмите "Enter".')
