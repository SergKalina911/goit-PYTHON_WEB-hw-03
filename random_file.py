""" Module to generate random files and folders for testing purposes."""

import shutil
from pathlib import Path
from random import randint, choice, choices


MESSAGE = "Hello, Привіт"


def get_random_filename():
    """ Генерує випадкове ім'я файлу довжиною 8 символів. """
    
    random_value = '()+,-0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz' \
                   '{}~абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    return ''.join(choices(random_value, k=8))


def generate_text_files(path):
    """ Генерує текстові файли з різними розширеннями. """
    
    documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    with open(path / f"{get_random_filename()}.{choice(documents).lower()}", "wb") as f:
        f.write(MESSAGE.encode())


def generate_archive_files(path):
    """ Генерує архівні файли з різними розширеннями. """
    
    archive = ('ZIP', 'GZTAR', 'TAR')
    shutil.make_archive(f"{path}/{get_random_filename()}", f'{choice(archive).lower()}', path)


def generate_folders(path):
    """ Генерує випадкову структуру папок. """
    
    folder_name = ['temp', 'folder', 'dir', 'tmp', 'OMG', 'is_it_true', 'no_way', 'find_it']
    folder_path = Path(
        f"{path}/" + '/'.join(choices(folder_name, weights=[10, 10, 1, 1, 1, 1, 1, 1], k=randint(5, len(folder_name)))))
    folder_path.mkdir(parents=True, exist_ok=True)


def generate_folder_forest(path):
    """ Генерує ліс папок з випадковою глибиною. """
    
    # Генеруємо від 2 до 4 папок у лісі
    for i in range(0, randint(2, 5)):
        generate_folders(path)


def generate_random_files(path):
    """ Генерує випадкову кількість файлів у папці. """
    
    # Генеруємо від 3 до 6 файлів у папці
    for i in range(3, randint(5, 7)):
        function_list = [generate_text_files, generate_archive_files]
        choice(function_list)(path)


def parse_folder_recursion(path):
    """ Рекурсивно проходить по папках і генерує файли. """
    
    for elements in path.iterdir():
        if elements.is_dir():
            generate_random_files(path)
            parse_folder_recursion(elements)


def exist_parent_folder(path):
    """ Створює батьківську папку, якщо її немає. """
    
    path.mkdir(parents=True, exist_ok=True)


def file_generator(path):
    """ Головна функція для генерації файлів і папок. """
    
    exist_parent_folder(path)
    generate_folder_forest(path)
    parse_folder_recursion(path)

# Запуск генерації файлів і папок при виконанні модуля
if __name__ == '__main__':
    parent_folder_path = Path("Temp")
    file_generator(parent_folder_path)
    print(f"Random files and folders have been generated in: {parent_folder_path.resolve()}")
       