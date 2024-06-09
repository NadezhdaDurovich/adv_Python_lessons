#Урок 5. Интераторы и генераторы
# Однострочники
# Обмен значения переменных:


# Распаковка значений:
# a, b, c = input('Три символа: ')
# print(f'{a =}, {b = }, {c = }')

# a, b, c = ('Один', 'Два', 'Три')
# print(f'{a =}, {b = }, {c = }')
# a, b, c = ('Один', 'Два', 'Три', 'Четыре') 
# print(f'{a =}, {b = }, {c = }')# Выдаст ошибку, т.к. количество элементов не совпадает с количеством переменных

# Но можно обойти это:
# data = ['Один', 'Два', 'Три', 'Четыре', 'Пять',] 
# Распаковка  коллекции с упаковкой “лишнего”
#a, b, c, *d = data 
#a, b, *c, d = data 
#a, *b, c, d = data 
# *a, b, c, d = data 
# print(f'{a =}, {b = }, {c = }, {d =}')

#Если нам нужна часть данных в переменных, а упакованный список в дальнейших расчётах не участвует, в качестве переменной используют подчеркивание:
# link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
# prefix, *_, suffix = link.split('/')

# Распаковка элементов коллекции. Длинный вариант вывода элементов последовательности в одну строку с разделителем табуляцией:
# data = [2, 4, 6, 8, 10, ]
# for item in data:
#     print(item, end='\t')

# И аналогичная операция в одну строку с распаковкой:
# data = [2, 4, 6, 8, 10, ]
# print(*data, sep='\t')

# Множественное присваивание
# a = b = c = 0
# a += 42
# print(f'{a=} {b=} {c=}') # подобная запись допустима только с неизменяемыми типами данных

# a = b = c = {1, 2, 3}
# a.add(42)
# print(f'{a=} {b=} {c=}')

# a, b, c = 1, 2, 3
# print(f'{a=} {b=} {c=}')

# t = 1, 2, 3
# print(f'{t=}, {type(t)}') # получим кортеж

# Множественное сравнение
# Аналогично присваиванию можно сравнить несколько переменных внутри конструкции if.
# a = b = c = 42
# # if a == b and b == c:
# if a == b == c:
#     print('Полное совпадение')
# if a < b < c:
#     print('b больше a и меньше c')

# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e)

# iter(object[, sentinel]). 
# a = 42
# iter(a) # TypeError: 'int' object is not iterable

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(list_iter)

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(*list_iter)
# print(*list_iter)

# import functools
# f = open('mydata.bin', 'rb')
# for block in iter(functools.partial(f.read, 16), b''):
#     print(block)
# f.close()

# next(iterator[, default]). 

# data = [2, 4, 6, 8]
# list_iter = iter(data)

# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter)) # StopIteration

# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter,42))
# print(next(list_iter, 42)) # StopIteration

# Генераторы похожи на итераторы тем, что возвращают некую последовательность значений но при этом не хранят данные в памяти, а вычисляют их по мере необходимости, чтобы вернуть очередное значение.

# a = range(0, 10, 2)
# print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
# b = range(-1_000_000, 1_000_000, 2)
# print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# Генераторные выражения Python позволяют создать собственный генератор, перебирающий значения.
# my_gen = (chr(i) for i in range(97, 123))
# print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
# for char in my_gen:
#     print(char)

# Комбинации for и if в генераторах и выражениях
#В общем виде 
#gen = (expression for expr in sequense1 if condition1
#     for expr in sequense2 if condition2
#     for expr in sequense3 if condition3
#     ...
#     for expr in sequenseN if conditionN)
# # в обычном коде
# for expr in sequense1:
#     if not condition1:
#         continue
# for expr in sequense2:
#     if not condition2:
#         continue
# ...
# for expr in sequenseN:
#     if not conditionN:
#         continue

#  Для каждого витка внешнего цикла внутренний перебирает все элементы от начала до конца. Например:
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res)=}\n{res}')

# List comprehensions

# my_listcomp = [chr(i) for i in range(97, 123)]
# print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
# for char in my_listcomp:
#     print(char, end =' ')

#Например выбираем все чётные числа из исходного списка и складываем их в результирующий.

# Длинный код:

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = []
# for item in data:
#     if item % 2 == 0:
#         res.append(item)
# print(f'{res = }')

# Код с использованием синтаксического сахара listcomp:

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = [item for item in data if item % 2 == 0]
# print(f'{res = }')

# Примущестава:
# 1. Не создаём пустой список в начале.
# 2. Не пишем двоеточия после цикла и логической проверки.
# 3. Исключаем метод append.
# Итого вместо 4 строк кода получаем одну.

# Генераторные выражения или генерация списка 

# Если на выходе нужен  готовый список, оптимальным будет следующий код:
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
# print(f'{len(res)=}\n{res}')

#А если нам не нужны все элементы разом, подойдет генераторное выражение без преобразования в список.
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# for item in mult:
#     print(f'{item = }')

# Set comprehensions

# Для множеств используются фигурные скобки
# my_setcomp = {chr(i) for i in range(97, 123)}
# print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... } 
# for char in my_setcomp:
#     print(char, end = ' ')

# Стоит обратить внимание на следующие особенности:
# ● порядок элементов внутри множества может не совпадать с порядком добавления элементов.
# ● множество хранит только уникальные значения 

# Dict comprehensions (генерация словаря):

# my_dictcomp = {i: chr(i) for i in range(97, 123)}
# print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
# for number, char in my_dictcomp.items():
#     print(f'dict[{number}] = {char}')

# data = {2, 4, 4, 6, 8, 10, 12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1, res2, res3)

# Создание функции генератора

# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

# функция yield запоминает своё состояние: строку, на которой остановилось выполнение, значения локальных переменных.
# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
# # for i, num in enumerate(factorial(10), start=1):
# #     print(f'{i}! = {num}')

# # Функции iter и next могут работать с созданными генераторами. Например так:
# my_iter = iter(factorial(4))
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter)) # StopIteration
