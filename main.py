# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""Цель задания:

Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:

Ключевая идея – использование вложенного for

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},
     Родительская директория: {parent_dir}')"""
import os  # Импортируем модуль os для работы с файловой системой
import time  # Импортируем модуль time для работы с временем

directory = "."  # Устанавливаем переменную directory равной текущей директории

# Используем цикл os.walk для обхода всех файлов и директорий в указанной директории
for root, dirs, files in os.walk(directory):
    # Для каждого файла в списке files
    for file in files:
        # Формируем полный путь к файлу, объединяя текущий путь root и имя файла
        filepath = os.path.join(root, file)
        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        # Форматируем время для отображения в удобном виде
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # Получаем размер файла
        filesize = os.path.getsize(filepath)
        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)
        # Выводим информацию о файле: имя файла, путь к файлу, размер, время изменения и родительскую директорию
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')