# Класс/тип, место в памяти и хэш объектов

# print('Введите любой текст: ')
# text = input()
# print(type(text), id(text), hash(text))


# Аннотация типов

# a: int | float = 42 # аннтотация типов не обязательна, важна, скорее, для самих разраотчиков, для упрощения чтения кода
# b: float = float(input("Введите число: "))
# print(a / b)

# def my_func(data: list[int,float]) -> float:
#     res = sum(data) / len(data)
#     return res

# print(my_func([2, 5.5, 15, 8.0, 13.74]))

# Атрибуты и методы объектов

# print('Hello,world!'.__doc__) # описание объекта(документация)
# print(str.__doc__)

# print('Hello,world!'.upper())  # перевод строки в верхний регистр
# print('Hello,world!'.count('l')) # подсчет кол-ва букв 'l' в строке

# print(dir('Hello,world!')) # перечисляет все доступные для объекта методы

# help('Hello,world!')
# help(str)
# help()

# Простые объекты 

# Целые числа

# x = int("42")
# y = int(3.1415)
# z = int('hello',base=30) # base - указатель на 30-теричную систему счисления

# print(x,y,z, sep='\n')

# import sys

# STEP = 2 ** 16
# num = 1

# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP

# number = 7_901_123_456_789 #  в данном случае _ - это разделитель разрядов

# number = 2 ** 16 - 1

# b = bin(number) # так число выглядит в двоичной системе исчисления  - это строковое значение
# o = oct(number) # так число выглядит в восьмеричной системе счисления - это строковое значение
# h = hex(number) # так число выглядит в шестнадцатеричной системе счисления - это строковое значение

# print(b, o, h)

# Вещественные числа

# print(0.1 + 0.2) # float делает расчет более точным - 0,30000000000000004
# pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
# print(pi) # при печати число ПИ "потеряло " часть своего "хвоста", т.к. тип float не резиновый !

# Логические типы (неявные логические преобразования в Python)

# DEFAULT = 42 #  В Python для объекта bool если 0 - False, а если >0 - True
# num = int(input("Введите уровень или ноль для значения по умолчаниюЖ "))
# level = num or DEFAULT
# print(level)

# name =  input("Как Вас зовут? ")
# if name:
#     print('Привет, ' + name ) # если польователь ввел имя --> True
# else:
#     print("Анонимус, приветствую!") # если пользователь пропустил ввод --> False

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# while data:
#     print(data.pop())

# Строки

# txt = 'Книга называется "Война и мир".'
# long_text = 'Это очень, очень и очень длинный текст, который не уместится в одну строку, так как рекомендованное количество символов в одной строке'\
#             ' не должно превышать восемьдесят символов.'
# print(long_text)


# LIMIT = 120 
# ATTENTION = "Внимание!"
# name = input('Ваше Имя: ')
# age = int(input('Ваш возраст: '))
# text = ATTENTION + ' Уважаемый(ая) ' + name + " Хоть Вам и осталось " + str(100 - age) +\
#                     ' года до ста лет, но длина строки не должна превышать ' + str(LIMIT) + ' символов.'
# print(text)

# empty_str = ''
# en_str = 'Text' 
# ru_str = 'Текст'
# unicode_str = ":), :D, :/, (:"
# print (empty_str.__sizeof__())
# print (en_str.__sizeof__())
# print (ru_str.__sizeof__())
# print (unicode_str.__sizeof__())

# Не получилось - дорабоать!)
# text = input("Введиит любой текст: ")
# if str.isalnum(text):
#     print(bin(text), oct(text), hex(text))

# else:
#     if str.isascii(text):
#         print("Текст написан в ASCII")
#     else:
#         print('Текст не написан в ASCII')


# Математические модули

# import math 

# print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n' )
# print(dir(math)) # Все досупные методы модуля
# print(help(math.gcd)) # напоминалка, что означает тот или иной модуль

# import decimal # вещественные числа

# print(0.1 + 0.2)
# pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
# print(pi)
# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num)

# decimal.getcontext().prec = 120 # метод .prec устанавливает точность 120 символов на вещественное число
# science = 2 * pi * decimal.Decimal(23.452346) ** 2
# print(science)



# import fractions # дроби

# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)

# Комплексные числа

# a = complex(2, 3)
# b = complex('2+3j')
# print(a, b, a == b, sep='\n ')

# Математические функции "из коробки"
print(abs(-10))
print(divmod(41, 40))
print(pow(2, 8))
print(round(2.3546, 2))