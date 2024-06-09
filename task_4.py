# a = 42
# print(type(a),id(a))
# # Функции высшего порядка
# print(type(id)) # функция id() передается как аргумент для функции type()
# very_bad_programmimg_styyle = sum
# print(very_bad_programmimg_styyle([1,2,3]))

# def my_func(): # пример функции без параметров/аргументов
#     pass

# def quadratic_equations (a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | None:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) /  (2 * a), (-b - d ** 0.5) /  (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return None # Можно это не писать,python сам допишет

# print(quadratic_equations(2, -3, -9))

# Неизменяемые аргументы
# def no_mutable(a: int) -> int:
#     a += 1
#     print(f'In func {a = }') # для демонстрации работы но не для привычки принтить из функции
#     return a

# a = 42
# print (f'Im main {a = }')
# z = no_mutable(a)
# print(f'{a = }\t{z= }')

# Изменяемые аргументы
# def mutable(data: list[int]) -> list[int]:
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }') # для демонстрации работы но не для привычки принтить из функции
#     return data

# my_list = [2, 4, 6, 8]
# print (f'Im main {my_list = }')
# new_list = mutable(my_list)
# print(f'{my_list = }\t{new_list= }')

# Значения по умолчанию
# def quadratic_equations (a, b=0, c=0): # при определении значений по умолчанию пробелы не ставятся
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) /  (2 * a), (-b - d ** 0.5) /  (2 * a)
#     elif d == 0:
#         return -b / (2 * a)


# print(quadratic_equations(2, -9))

# def from_one_to_n(n, data=[]):
#     for i in range(1, n + 1):
#         data.append(i)
#     return data
# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }') #  в данном случае каждый раз функция ссылается на один и тот же объект data, дополняя список новыми элементами
# Чтобы этого избежать, применяется следующий прием:

# def from_one_to_n(n, data=None):
#     if data is None:
#         data =[]
#     for i in range(1, n + 1):
#         data.append(i)
#     return data
# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')

# Ключевые и позиционные параметры

# def func(positional_onle_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
#     pass

# def standart_arg(arg):
#     """Пример обычной функции"""
#     print(arg) # Приним дял примера, а не для привычки

# standart_arg(42)
# standart_arg(arg=42) # всё работает

# def standart_arg(arg, /):
#     """Пример только позиционной функции"""
#     print(arg) # Приним дял примера, а не для привычки

# standart_arg(42)
# standart_arg(arg=42) # ошибка - нельзя передать ключевой аргумент!

# def standart_arg(*, arg):
#     """Пример только ключевой функции"""
#     print(arg) # Приним дял примера, а не для привычки

# standart_arg(42) # ошибка - нельзя передать позиционныей аргумент!
# standart_arg(arg=42) 

# def combained_example(pos_only, /, standart, * kwg_only):
#     """Пример функции со всеми вариантами параметров"""
#     print(pos_only, standart, kwg_only) # Приним дял примера, а не для привычки

# combained_example(1, 2, 3) # ошибка - нельзя передать больше 2-х позиционных аргументов!
# combained_example(1, 2, kwd_only=3) 
# combained_example(1, standart=2, kwd_ony=3) 
# combained_example(pos_only=1,standart=2, kwd_ony=3) # ошибка - нельзя передать больше 2-х ключевых аргументов!

def func(*args): # - принимает любоe число позиционных аргументов
    pass
def func(**kwargs): # - принимает любоe число ключевых аргументов
    pass
def func(*args, **kwargs): # - принимает любоe число позиционных и ключевых аргументов
    pass

# def mean(args):
#     return sum(args) / len(args)
# print(mean([1, 2, 3]))
# print(mean(1, 2, 3)) # выдаст ошибку, т.к. может быть передан лишь один позиционный аргумент

# def mean(*args):
#     return sum(args) / len(args)
# print(mean(*[1, 2, 3])) # c помощью * мы распаковываем список и передаем элементы как отдельные объекты 
# print(mean(1, 2, 3)) # выдаст ошибку, т.к. может быть передан лишь один позиционный аргумент

# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету "{key}" получена оценка {value}')
# school_print(химия=5, физика=4, математика=5, физра=5)

# Локальные переменные:
# def func(y: int) -> int:
#     x = 100
#     x += 100 
#     print(f'In func {x = }') # Только для демонстрации работы, обычно из функции мы не принтим!
#     return y + 1
# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }')

# def func(y: int) -> int:
#     x += 100 # функция выдаст ошибку, т.к. переменная x внутри функции ранее не была определена
#     print(f'In func {x = }') # Только для демонстрации работы, обычно из функции мы не принтим!
#     return y + 1
# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }') 

# Глобальные переменные
# def func(y: int) -> int:
#     global x
#     x += 100
#     print(f'In func {x = }') # Только для демонстрации работы, обычно из функции мы не принтим!
#     return y + 1
# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }') 

# Не локальные переменные
# def main(a):
#     x = 1
    
#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }') # Только для демонстрации работы, обычно из функции мы не принтим!
#         return y + 1
    
#     return x + func(a)
# x = 42
# print(f'In main {x = }')
# z = main(x)
# print(f'{x = }\t{z = }') 

# Константы используются в функциях:
# LIMIT = 1000

# def func(x, y):
#     result = x ** y % LIMIT
#     return result

# print(func(42, 73))

# Синтаксический сахар - это анонимная lambda-функция:

# def add_to_def(a, b):
#     return a + b

# add_to_lambda = lambda a, b: a + b # такое применение лямбда-функции не приветствуется! 

# print(add_to_def(42, 3.14))
# print(add_to_lambda(42, 3.14))


# my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
# s_key = sorted(my_dict.items())
# s_value = sorted(my_dict.items(), key=lambda x: x[1])
# print(f'{s_key = }\n{s_value = }')

#Пример документации функции:
# def max_before_hundred(*args):
#     """Return the maximum number not exceeding hundred.

#     :param args: tuple of int or float numbers
#     :return: int or float number from the tuple args
#     """
#     m = float('-inf')
#     for item in args:
#         if m < item < 100:
#             m = item
#     return m

# print(max_before_hundred(+42, 73, 256, 0))
# help(max_before_hundred)

# #map(function, iterable)

# texts = ['Привет!', 'Здорова!', 'Приветствую!']
# res = map(lambda x: x.lower(), texts)
# print(*res)
#filter(function, iterable)
# numbers = [42, -73, 1024]
# res = tuple(filter(lambda x: x > 0, numbers))
# print(res)

# zip(*iterables, strict=False)

# names = ['Иван', 'Ниолай', 'Петр']
# salaries = [125000, 96000, 109000]
# awards = [0.1, 0.125, 0.13, 0.99]
# for name, salary, award in zip(names, salaries, awards):
#     print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

# max(iterable, *[, key, default]) или max(arg1, arg2, *args[, key])

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 =[('Иван', 125000), ('Николай', 96000), ('Петр', 109000)]
# print(max(lst_1, default='empty'))
# print(max(*lst_2))
# print(max(lst_3, key=lambda x: x[1]))

# min(iterable, *[, key, default]) или min(arg1, arg2, *args[, key])

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 =[('Иван', 125000), ('Николай', 96000), ('Петр', 109000)]
# print(min(lst_1, default='empty'))
# print(min(*lst_2))
# print(min(lst_3, key=lambda x: x[1]))

# sum(iterable, /, start=0)

# my_list = [42, 256, 73]
# print(sum(my_list))
# print(sum(my_list, start=1024))

# all(iterable)

# def all_(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


# numbers = [42, -73, 1024]
# if all(map(lambda x: x > 0, numbers)):
#     print('Все элементы положительные')
# else:
#     print('В послеовательности есть отрицательные и/или нулевые элементы')


# any(iterable)

# def any_(iterable):
#     for element in iterable:
#         if not element:
#             return True
#     return False

# numbers = [42, -73, 1024]
# if any(map(lambda x: x > 0, numbers)):
#     print('Хотя бы один элемент положительный')
# else:
#     print('Все элементы не больше нуля')


# chr(integer) # выдает символ по юникоду

print(chr(97))
print(chr(1105))
print(chr(128519))

# ord(char) # выдает юникод по символу

print(ord('a'))
print(ord('а'))
print(ord("😇"))