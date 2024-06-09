# Задание 1. Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

# list = [1, 2, 3, 1, 2, 3]
# print(set(list))

# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# Задание 2. Пользователь вводит данные. Сделайте проверку данных и преобразуйте, если возможно, в один из вариантов ниже:
# а) Целое положительное число; б) Вещественное положительное или отрицательное число; в) Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква;
# г) Строку в верхнем регистре в остальных случаях

# data = input('Введите что-нибудь: ')
# if data.isdecimal():
#     print(f'{int(data)} - целое число')
# else:
#     try:
#         print(f'{float(data)} - вещественное число')
#     except ValueError:
#         if data.lower() != data:
#             print(data.lower())
#         else:
#              print(data.upper())

# Звдание 3. Создайте вручную кортеж содержащий элементы разных типов. Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

# my_turple = (1, 2.3, 'hi', [1,2,3])
# new_dict = {}
# for item in my_turple:
#     t = type(item).__name__
#     if t not in new_dict:
#         new_dict[t] = []
#     new_dict[t].append(item)
# print(new_dict)

    
# Задание 4. Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды

# from collections import Counter

# my_list = [1, 1, 1, 5, 4, 7 , 7, 8, 9, 9, 10]
# dic2 = Counter(my_list) # встроеная функция "счетчик" сортирует данные по убыванию счетчиков
# dictionary = {}
# for item in my_list:
#     if item not in dictionary:
#         dictionary[item] = 0
#     dictionary[item] += 1 # dictionary[item] = dictionary.get(item,0)
# print(dictionary)

# for k,v in dictionary.items():
#     if v == 2:
#         my_list.remove(k) # remove удаляет только одно нахождение, поэтому пропишем несколько раз
#         my_list.remove(k)
# print(my_list)
# print (dic2)

# Задание 5. Создайте вручную список с повторяющимися целыми числами. Сформируйте список с порядковыми номерами нечётных элементов исходного списка. Нумерация начинается с единицы.
# my_list = [1, 1, 1, 5, 4, 7 , 7, 8, 9, 9, 10]
# special_list = []
# for i, elem in enumerate(my_list,1):
#     if elem % 2 == 1:
#         special_list.append(i)
# print(special_list)

 
# Задание 6. Пользователь вводит строку текста. Вывести каждое слово с новой строки. Слова нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode. Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# text = input('Введите строку: ').split()
# text.sort() # удалить для примеров с русским текстом
# max_len = max([len(word) for word in text])
# max_len1 = len(max(text, key=len))

# for i, word in enumerate(text, 1):
#     print(f'{i} {word:>{max_len}}')

# Задание 7. Пользователь вводит строку текста. Подсчитайте, сколько раз встречается каждая буква в строке без использования метода count и с ним. 
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.  Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

# from collections import Counter

# new_text = input('Введите строку: ')

# print(Counter(new_text)) # встроенное решение

# dict_new = {}
# for letter in new_text:
#     dict_new[letter] = new_text.count(letter) 
# print(dict_new)

# Задание 8. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга? Какие вещи уникальны, есть только у одного друга? Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

# things = {
#     'Юра': ('палатка', 'рюкзак', 'котелок'),
#     'Сергей': ('рюкзак', 'палатка', 'спички', 'лопата'),
#     'Олег': ('стол', 'рюкзак', 'продукты'),
# }
# first = list(things.keys())[0]
# res = set(things[first])
# for k, v in things.items():
#     res = res.intersection(set(v))

# print('У всех путешественников есть ', res)

# dict_count = {}
# for k, v in things.items():
#     for value in v:
#         dict_count[value] = dict_count.get(value, 0) + 1

# friends = len(list(things.keys())) - 1 
# dict_things = []

# for k, v in dict_count.items():
#     if v == friends:
#         dict_things.append(k)
# for k, v in things.items():
#     for item in dict_things:
#         if item not in v:
#             print(f'{item} отсутствует у путешественника с именем {k}')
#             break
# one_thing = []
# for k,v in dict_count.items():
#     if v == 1:
#         one_thing.append(k)
# print(f'Вещи в единственном экземпляре - {one_thing}')


