# JSON (JavaScript Object Notation) — это популярный формат текстовых данных,который используется для обмена данными в современных веб- и мобильных приложениях. 

# JSON - самый популярный формат сериализации

# Python          JSON            Python

# dict            object          dict
# list, tuple     array           list
# str             string          str
# int             number (int)    int
# float           number (real)   float
# True            true            True
# False           false           False
# None            null            None

# Преобразование JSON в Python:

import json

# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f) # загрузка JSON из файла и сохранение в dict или list

# print(f'{type(json_file) = }\n{json_file = }') # выводим тип преобразованных данных (словарь) и сами данные
# print(f'{json_file["name"] = }') # обращаемся к элементам словаря по ключу
# print(f'{json_file["address"]["geo"] = }')
# print(f'{json_file["email"] = }')

# json_text = """ # задан текст (несколько объектов) json
# [
#     {
#     "userId": 1,
#     "id": 9,
#         "title": "nesciunt iure omnis dolorem tempora et accusantium",
#         "body": "consectetur animi nesciunt iure dolore"
#     },
#     {
#         "userId": 1,
#         "id": 10,
#         "title": "optio molestias id quia eum",
#         "body": "quo et expedita modi cum officia vel magni"
#     },
#     {
#         "userId": 2,
#         "id": 11,
#         "title": "et ea vero quia laudantium autem",
#         "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
#     },
#     {
#         "userId": 2,
#         "id": 12,
#         "title": "in quibusdam tempore odit est dolorem",
#         "body": "praesentium quia et ea odit et ea voluptas et"
#     }
# ]"""

# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text) # загрузка JSON из строки и сохранение в dict или list
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list =}')

# Преобразование Python в JSON

# my_dict = { # создаем словарь
#     "first_name": "Джон",
#     "last_name": "Смит",
#         "hobbies": ["кузнечное дело", "программирование","путешествия"],
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Алиса",
#             "age": 5
#         },
#         {
#             "first_name": "Маруся",
#             "age": 3
#         }
#     ]
# }
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f:  # открываем файл для записи и сохраняем содержимое функцией dump
#     json.dump(my_dict, f) # сохранение dict или list в файле в виде JSON


# Проведём десериализацию и проверим целостность данных
# with open('new_user.json', 'r', encoding='utf-8') as f: 
#     new_dict = json.load(f)
# print(f'{new_dict = }')

# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование","путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
# dict_to_json_text = json.dumps(my_dict) # сохранение dict или list в виде JSON строки
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# ● Дополнительные параметры dump и dumps

# res = json.dumps(my_dict, indent=2,  separators=(',', ':'),  sort_keys=True)
#● Параметр indent отвечает за форматирование с отступами
#● Параметр separators принимает на вход кортеж из двух строковых элементов.
#   Первый — символ разделитель элементов.
#   Второй — разделитель ключа и значения.
#● Параметр sort_keys=True отвечает за сортировку ключей по алфавиту (по умолчанию - ложь)

# my_dict = {
#     "id": 123,
#     "name": "Clementine Bauche",
#     "username": "Cleba",
#     "email": "cleba@corp.mail.ru",
#     "address": {
#         "street": "Central",
#         "city": "Metropolis",
#         "zipcode": "123456"
#     },
#     "phone": "+7-999-123-45-67"
# }
# res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
# print(res)

# a = 'Hello world!'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b, indent=3, separators=('; ', '= ')) # замена запятой на ; а знака двоеточия на знак = приведет к формированию текста похожего на json, но все -таки не json
# print(c)

# CSV (от англ. Comma-Separated Values — значения, разделённые запятыми) — текстовый формат, предназначенный для представления табличных данных. 

# Рассмотрим тестовый CSV файл biostats.csv:

# Чтение CSV

import csv

# with open('biostats.csv', 'r', newline='') as f: # параметр newline='' необходимо указывать во время открытия файла.
#     csv_file = csv.reader(f) # Функция csv.reader принимает на вход файловый дескриптор и построчно читает информацию
#     for line in csv_file:
#         print(line)
#     print(type(line))

# Другой Файл biostats_tab.csv хранит те же данные, что и файл biostats.csv, но вместо разделителя ',' используется символ табуляции. 
# По сути это разновидность TSV — файл с разделителем табуляцией.


# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)
#     print(type(line))
# ➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
# ➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу, указывающую функции, что числа без кавычек необходимо преобразовать к типу float.

# ● Запись CSV
# ● csv_write = csv.writer(f) csv_write позволяет сохранять данные в формате CSV
# ● csv_write.writerow(line) сохранение списка в одной строке файла в формате CSV
# ● csv_write.writerows(all_data) сохранение матрицы в нескольких строках файла в формате CSV

# Используя менеджер контекста with открыли два файла. Из первого читаем информацию, а второй создаём для записи.
# with (open('biostats_tab.csv', 'r', newline='') as f_read, open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write):
#     csv_read = csv.reader(f_read, dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC) #Ф ункция reader возвращает объект csv_read для чтения
#     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) # Функция writer возвращает объект csv_write для записи. 
#     all_data = []
#     for i, line in enumerate(csv_read): # В цикле читаем все строки из исходного файл. 
#         if i == 0:
#             csv_write.writerow(line) # строку с заголовком сразу записываем методом writerow.
#         else:
#             line[2] += 1 # Для остальных строк увеличиваем возраст на единицу           
#             for j in range(2, 4 + 1):
#                 line[j] = int(line[j]) # преобразуемвещественные числа в целые
#             all_data.append(line) # сохраняем список в матрицу all_data
#     csv_write.writerows(all_data) # Одним запросом сохраняем матрицу в файл.

# ● Чтение в словарь
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex","age", "height", "weight", "office"],restkey="new", restval="MainOffice", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')
# ● fieldnames — список заголовков столбцов, ключей словаря
# ● restkey — значение ключа для столбцов, которых нет в fieldnames
# ● restval — значение поля для ключей fieldnames, которых нет в файле CSV

# Запись CSV из словаря
# Параметры класса DictWriter аналогичны параметрам DictReader
# ● csv_write.writeheader() сохранение первой строки с заголовками в порядке их перечисления в параметре fieldnames
# ● csv_write.writerow(line) сохранение списка в одной строке файла в формате CSV
# ● csv_write.writerows(all_data) сохранение матрицы в нескольких строках файла в формате CSV

# Сериализация
# import pickle
# ● pickle.dump(my_dict, f) сохранение объекта в бинарном файле
# ● result = pickle.dumps(my_dict) сохранение объекта в строку байт

# Десериализация
# ● new_dict = pickle.load(f) загрузка из бинарного файла и сохранение в объекта
# ● new_dict = pickle.loads(data) получение объекта из бинарной строки