# Задача 1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# BASE = 16
# number = int(input("Введите число: "))
# print(hex(number))
# values = '0123456789ABCDEF'
# result = " "
# while number > 0:
#     result = values[number % BASE] + result
#     number //= BASE
# print(result)


# Задача 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions
# ввод числителей и знаменателей двух дробей 
# a = int(input("Введите числитель первой дроби: ")) 
# b = int(input("Введите знаменатель первой дроби: ")) 
# c = int(input("Введите числитель второй дроби: ")) 
# d = int(input("Введите знаменатель второй дроби: ")) 

# # нахождение произведения дробей 
# numerator_mult = a * c 
# denominator_mult = b * d 

# # сокращение дроби 
# def gcd(a, b): 
#     if b == 0:  
#         return a 
#     else: 
#         return gcd(b, a % b) 

# divisor = gcd(numerator_mult, denominator_mult) 
# numerator_mult //= divisor 
# denominator_mult //= divisor 

# # вывод результата 
# print(f'Произведение дробей {a}/{b} и {c}/{d} равно: {numerator_mult}/{denominator_mult}')

# # нахождение cуммы дробей 
# def lcm(a, b):  #Нахождение наименьшего общего кратного двух чисел
#     if a == 0 or b == 0: 
#         return 0 
#     else: 
#         return abs(a * b) // gcd(a, b)

# common_denominator = lcm(b, d)  # Находим общий знаменатель 
#   # Приводим первую дробь к общему знаменателю 
# a *= (common_denominator // b)
# b = common_denominator 
     
# # Приводим вторую дробь к общему знаменателю 
# c *= common_denominator // d 
# d = common_denominator 

# # Складываем дроби 
# numerator_sum = a + c 
# # Сокращаем дробь 
# divisor = gcd(numerator_sum, common_denominator) 
# numerator_sum //= divisor
# common_denominator //= divisor
# # вывод результата 
# print(f'Cумма дробей {a}/{b} и {c}/{d} равна {numerator_sum}/{common_denominator}')

# print('Проверим себя с помощью модуля fractions')
# import fractions # дроби
# f1 = fractions.Fraction(a, b)
# f2 = fractions.Fraction(c, d)
# print(f'Произведение заданных дробей: {f1 * f2}')
# print(f'Сумма заданных дробей: {f1 + f2}')
