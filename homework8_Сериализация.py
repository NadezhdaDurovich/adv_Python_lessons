# Задание 1

# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
#     ○ Для дочерних объектов указывайте родительскую директорию.
#     ○ Для каждого объекта укажите файл это или директория.
#     ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
# и директорий.

# Функция записана в модуль "directory_analysis.py"

from moduls_from_eighth_seminar import directory_analysis



# Задание 2
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

# Создан пекет с модулями "moduls_from_eighth_seminar"

from moduls_from_eighth_seminar.directory_analysis import analysis_directory_results
import os

my_list = os.listdir() # Функция listdir возвращает список файлов и каталогов.
analysis_directory_results(my_list)