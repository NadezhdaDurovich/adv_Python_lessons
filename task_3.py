# Коллекции данных

# Списки

# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# list_3 = []
# list_4 = [3.14, True, "Hello world!"]

# my_list = [2, 4, 6, 8, 10, 12]
# print(my_list[0])
# # print(my_list[6]) # IndexError: list index out of range
# print(my_list[-1])

# Методы работы со списками

# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a) # append добавляет элемент в список
# print(my_list)
# my_list.append(b)
# print(my_list)
# my_list.append(c)
# print(my_list)
# my_list.append(my_list)# это недопустимо
# print(my_list)

# my_list.extend(a) # TypeError: 'int' object is not iterable
# print(my_list)
# my_list.extend(b) # extend добавляет итерируемые элементы в конце списка
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list) # это допустимо
# print(my_list)

# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop() # pop удаляет послений элемент списка, сохраняя его в переменную
# print(spam, my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# err = my_list.pop(10) # IndexError: pop index out of range

# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.count(2) # Метод count подсчитывает вхождение элемента в список.
# print(spam)
# eggs = my_list.count(3)
# print(eggs)

# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.index(4) # Метод index возвращает индекс переданного объекта внутри списка
# print(spam)
# eggs = my_list.index(4, spam + 1, 90) # второй и третий агрументы - стартовое и финальное места в списке для поиска
# print(eggs)
# err = my_list.index(3) # ValueError: 3 is not in list

# my_list = [2, 4, 6, 8, 10, 12]
# my_list.insert(2, 555) # Метод insert принимает на вход два аргумента — индекс для вставки и объект вставки. Метод добавляет элемент после индекса.
# print(my_list)
# my_list.insert(-2, 13)
# print(my_list)
# my_list.insert(42, 73) # my_list.append(73)
# print(my_list)

# my_list = [2, 4, 6, 8, 10, 12, 6]
# my_list.remove(6) # Метод remove принимает на вход объект, производит его поиск в списке и удаляет в случае нахождения.
# print(my_list)
# # my_list.remove(3) # ValueError: list.remove(x): x not in list
# print(my_list)

# Сортировка списков, развороты

# Функция  sorted()


# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True) # сортировка по убыванию
# print(my_list, rev_list, sep='\n')

# Метод .sort()

# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort() # в отличие от функции sorted() Метод sort осуществляет сортировку элементов списка без создания копии, inplace. Метод применим только к спискам
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# Функция reversed()

# my_list = [4, 8, 2, 9, 1, 7, 2]
# # res = reversed(my_list) #Функция принимает на вход последовательность, а возвращает  объект итератор с обратным порядком элементов.
# # print(type(res), res)
# # rev_list = list(reversed(my_list)) # нужно создать новый список, чтобы увидеть рез-т!
# # print(rev_list)

# for item in reversed(my_list): # Такой приём позволяет работать с элементами списка внутри цикла в обратном порядке.
#     print(item)

# Метод .reverse()

#my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.reverse() # встроенный метод reverse разворачивает список на месте, не создавая копии
# print(my_list)

# Cинтаксический "сахар": После имени списка в квадратных скобках слитно записываем два двоеточия и минус один.

# new_list = my_list[::-1]
# print(my_list, new_list, sep='\n')

# Срезы

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:7:2]) # 1-й индекс - стартовый (элемент включается в срез), 2-й индекс - для остановки (элемент не вкючается в срез), 3-й индекс - длина шага
# print(my_list[:7:2]) # по умолчанию значение 1-го индекса - ноль (т.е. срез начинаем с нулевого элемента списка)
# print(my_list[2::2]) # пропущенное значение 2-го индекса означает, что срез делаем до конца списка
# print(my_list[2:7:]) # по умолчанию шаг = 1
# print(my_list[8:3:-1]) # отрицат.длина шага означает движение справа налево
# print(my_list[3::]) 
# print(my_list[:7:]) 

# Создание копий

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy() # создали поверхностную копию списка
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')

import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')

# Метод copy создал поверхностную копию, копию верхнего уровня. Изменения же вложенных объектов отразятся и на оригинале. В таком случае для создания 
# полной копии любой глубины вложенности используют функцию deepcopy из модуля copy.

# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')

# Измеряем длину

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(len(my_list))
# print(len(matrix))
# print(len(matrix[1]))


# Работа со строками как с массивами

# text = 'Hello world!'

# print(text[6])
# print(text[3:7])

# new_txt = text.replace('l', 'L', 2) # Третий аргумент (2) — максимальное количество замен. Если его не указывать, будут заменены все совпадения
# print(text, new_txt, sep='\n')

# print(text.count('l')) # подсчет кол-ва опре.элементов
# print(text.index('l')) # поиск идекса первого по счету элемента 
# print(text.find('l')) # аналоги index, но при отсутствии искомого элемента выдает результат -1 
# print(text.find('z'))

# print(text[::-1]) # разворот строки

# Форматирование строк

# name = 'Nadya'
# age = 38
# # text = 'Меня зовут %s и мне %d лет' % (name, age) # устаревший вариант
# # print(text)

# # text = 'Меня зовут {} и мне {} лет'.format(name, age) # часто используемый вариант до версии python 3.07
# # print(text)

# text = f'Меня зовут {name} и мне {age} лет' # современный вариант
# print(text)

# Уточнение формата

# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}') # :.2f — число пи выводим с точность два знака после запятой
# data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
# for item in data:
#     print(f'{item:>10}') # :>10 — элементы списка выводятся с выравниванием по правому краю и общей шириной вывода в 10 символов
# num = 2 * pi * data[1]
# print(f'{num = :_}') # :_ — число разделяется символом подчёркивания для деления на блоки по 3 цифры.


# Методы строк

# метод .split()

# link = 'https://habr.com/ru/users/dzhoker1/posts/'
# urls = link.split('/') # Метод split позволяет разбить строку на отдельные элементы в соответствии с разделителем и поместить результат в список
# print(urls)
# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)

# a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()

# метод .join()

# data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts']
# url = '/'.join(data)
# print(url)


# Методы upper, lower, title, capitalize

# text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())


# Методы startswith и endswith

# text = 'Однажды в студёную зимнюю пору'
# print(text.startswith('Однажды')) # Метод startswith проверяет начинается ли строка с заданной подстроки (возвращает истину или ложь)
# print(text.endswith('зимнюю', 0, -5)) # Метод endswith проверяет окончание строки переданной в качестве аргумента подстрокой.

# Оба метода помимо подстроки могут принимать параметры start и stop. В этом случае проверка начала либо конца будет проводиться в указанном диапазоне.

# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>25}')

# Кортежи

# Создать кортеж можно четырьмя способами.
# a = ()
# b1 = 1,
# b2 = (1,)
# c1 = 1, 2, 3,
# c2 = (1, 2, 3)
# d = tuple(range(3))
# print(a, b1, b2, c1, c2, d, sep='\n')

# Общие операции

# my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
# print(my_tuple[2:6:2])
# print(my_tuple[-3])
# print(my_tuple.count(2))
# print(f'{my_tuple = }')
# print(my_tuple.index(2, 2))
# print(type('text',))

# Cловари

# Способы создания словаря

# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
# b = dict(one=42, two=3.14, ten='Hello world!')
# c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
# print(a == b == c)

# Добавление нового ключа
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# print(my_dict)

# Доступ к значению словаря (через квадратные скобки [])
# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict['two'])
# print(my_dict[TEN])
# #print(my_dict[1]) # KeyError: 1
# print(my_dict.get('two'))
# print(my_dict.get('five'))
# print(my_dict.get('five', 5))
# print(my_dict.get('ten', 5))

# Методы словарей

# Метод setdefault

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

# spam = my_dict.setdefault('five') # Метод setdefault похож не get, но отсутствующий ключ добавляется в словарь.
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# new_spam = my_dict.setdefault('two')
# print(f'{new_spam=}\t{my_dict=}')
# new_eggs = my_dict.setdefault('one', 1_000)
# print(f'{new_eggs=}\t{my_dict=}')

# Метод keys

# print(my_dict.keys()) # Метод keys возвращает объект-итератор dict_keys.
# метод keys применяется в связке с циклом for для перебора ключей словаря.
# for key in my_dict.keys():
#     print(key)

# Метод values

# print(my_dict.values()) # Метод values похож на keys, но возвращает значения в виде объекта итератора dict_values, а не ключи
# for value in my_dict.values():
#     print(value)

# Метод items

# print(my_dict.items()) # Если в цикле необходимо работать одновременно с ключами и значениями, как с парами, используют метод items.
# for tuple_data in my_dict.items():
#     print(tuple_data)
# for key, value in my_dict.items():
#     print(f'{key = } value before 100 - {100 - value}')

# Метод popitem
# spam = my_dict.popitem() # Для удаления пары ключ значение из словаря 
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict=}')

# Метод pop

# spam = my_dict.pop('two') # Метод pop удаляет пару ключ-значение по переданному ключу.
# print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six') # KeyError: 'six'
# err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0 

# Метод update

# my_dict.update(dict(six=6)) # Для расширение словаря новыми значениями
# print(my_dict)
# my_dict.update(dict([('five', 5), ('two', 42)]))
# print(my_dict)

# Ещё один способ создать словари из нескольких других, который появился в новой  версии Python — вертикальная черта
# new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
# print(new_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)

 # Множества set и frozenset

# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set) # двойка передавалась в множества дважды, но хранится в единственном экземпляре, как один из уникальных элементов
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'

# Методы множеств

# Метод add

my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# # my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
# my_set.add((9, 10))
# print(my_set)

# Метод remove
# my_set.remove(5)
# print(my_set)
# my_set.remove(10) # KeyError: 10

# Метод discard
# my_set.discard(5)
# print(my_set)
# my_set.discard(10) # В отличии от remove при попытке удалить несуществующий элемент discard не вызывает ошибку. При этом множество не изменяется.

#  Метод intersection
# other_set = {1, 4, 42, 314}
# # new_set = my_set.intersection(other_set) # Для получения множества с элементами, которые есть и в левом и в правам множестве 
# #  Исходные множества при пересечении не изменяются!
# # более современый вариант кода
# new_set = my_set & other_set
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Метод union

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set) #  объединениe множеств. На выходе получаем множество уникальных элементов из левого и правого множеств
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set # более современый вариант кода
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Метод difference

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set) # Метод difference удаляет из левого множества элементы правого/ На выходе получаем множество элементов встречающихся только в левом множестве
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set - other_set # более современый вариант кода
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Проверка на вхождение, in
# my_set = {3, 4, 2, 5, 6, 1, 7}
# print(42 in my_set) # Для проверки входит ли элемент в множество

# my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
# print(len(my_set))
# print(my_set - {1, 2, 3})
# print(my_set.union({2, 4, 6, 8}))
# print(my_set & {2, 4, 6, 8})
# # print(my_set.discard(10))


# Классы bytes и bytearray

# text_en = 'Hello world!'
# res = text_en.encode('utf-8')
# print(res, type(res))
# text_ru = 'Привет, мир!'
# res = text_ru.encode('utf-8')
# print(res, type(res))

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8') # неизменяемая последовательность
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8') # изменяемый массив данных
print(f'{x = }\n{y = }')

