# Задача 1. Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные. 
# a = 5
# b = 5.1
# c = 'Hello'
# d = [1, 2, 3, 4]
# e = {a, b, c}
# print(type(a), type(b), type(c), type(d), type(e))

# Задача 2. Создайте в переменной data список значений разных типов,перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы, значение, адрес в памяти, размер в памяти, хэш объекта, результат проверки на целое число, только если он положительный,
# результат проверки на строку, только если он положительный. Добавьте в список повторяющиеся элементы и сравните результаты.

# from typing import Hashable
# data = [5, 5.1, 'Hello', [1, 2, 3]]
# print(data)
# for i in range (len(data)):
#     print(f'Элемент № {i+1} - {data[i]}, ячека памяти {id(data[i])}, объем памяти {data[i].__sizeof__()}', end='\t')
#     print ('Целое число' if isinstance(data[i],int) else 'Не относится к целым числам', end='\t')
#     print ('Строка' if isinstance(data[i], str) else 'Не строка', end='\n')
#     print ('Хэш - ', {hash(data[i])} if isinstance(data[i], Hashable) else "Не хэшируется", end='\t')
#     print()
       
# data.insert(len(data), 1)
# print (data)

# Задача 3. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно: Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления Избегайте магических чисел
# Добавьте аннотацию типов, где это возможно

# BASE = 2
# number = int(input("Введите число: "))
# print(bin(number))
# result = " "
# while number > BASE:
#     result += str(number % BASE)
#     number //= BASE
# result += str(number)
# print(result[::-1])

# BASE = 8
# number = int(input("Введите число: "))
# print(oct(number))
# result = " "
# while number > BASE:
#     result += str(number % BASE)
#     number //= BASE
# result += str(number)
# print(result[::-1])

# Задача 4. Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не превышает 1000 у.е. 
# Точность вычислений должна составлять не менее 42 знаков после запятой.

# import decimal
# import math

# decimal.getcontext().prec = 50
# maximum = 1000
# d = decimal.Decimal(input('Введите диаметр круга до 1000: '))
# if d > maximum:
#     print('Слишком большое число')
# r = d / 2
# pi = decimal.Decimal(math.pi)
# s = pi * r ** 2
# long = 2 * pi * r

# print(f'Площадь круга c диаметром {d} равна {s}')
# print(f'Длина окружности круга c диаметром {d} равна {long}')

# Задача 5. Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный. 
# Используйте комплексные числа для извлечения квадратного корня.

# a = int(input("Введина значение a: "))
# b = int(input("Введина значение b: "))
# c = int(input("Введина значение c: "))

# d = b ** 2 - 4 * a * c
# if d > 0:
#     print((-b + d ** 0.5)/ (2 * a))
#     print((-b - d ** 0.5)/ (2 * a))
# elif d == 0:
#     print(-b/ (2 * a))
# else:
#     d = complex(d)
#     print((-b + d ** 0.5)/ (2 * a))
#     print((-b - d ** 0.5)/ (2 * a))

# Задача 6. Напишите программу банкомата. Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%. Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

from decimal import Decimal

MIN_SUM = 50
MIN_COMISSION = 30
MAX_COMISSION = 600
PERCENT_TO_TAKE = Decimal(0.015)
BONUS_COUNTER = 3
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX= 5000000
TAX_RATE = Decimal(0.1)

def menu(balance: Decimal, count: int, flag: bool):
    dct = {'1. ': '1. пополнить счет',
           '2. ': '2. снять со счета',
           '3. ': '3. выйти из программы'}
    
    for k,v in dct.items():
        if k.isdigit():
            print(f'{k}:{v}')
        else:
            print(v)
          
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)

    choice = input('Выберите команду:')
    if choice == '3':
        flag = False
        print(f'Баланс счета: {balance}.')
        return balance, flag
    elif choice == '1':
        balance = get_money(balance)
        count += 1
    elif choice =='2':
        balance = give_money(balance)
        count += 1
    else:
        print("Неверная команда")
       
    
    if count % BONUS_COUNTER == 0:
        balance *= (1+BONUS)
    
    print(f'Баланс счета: {balance}.')
    return balance, flag

def get_money(balance: Decimal):
    money_to_get = Decimal(input("Введите сумму пополнения: "))
   
    if money_to_get % MIN_SUM == 0:
        return balance + money_to_get
    else:
        print('Ошибка: сумма должна быть кратна 50. ')
        return balance, flag

def give_money(balance: Decimal):
    money_to_give = Decimal(input("Введите сумму снятия: "))
        
    if money_to_give % MIN_SUM == 0:
        percent = money_to_give * PERCENT_TO_TAKE
        
        if percent <  MIN_COMISSION:
            percent = MIN_COMISSION
        elif percent > MAX_COMISSION:
            percent = MAX_COMISSION
        
        if balance < (money_to_give + percent):
                print('Сумма снятия с комиссией за услугу больше доступного баланса.')
        else:
            balance -= (money_to_give + percent)
    else:
        print('Ошибка: сумма должна быть кратна 50. ')
            
    if count > BONUS_COUNTER:
        balance += (balance * BONUS)
    return balance, flag

if __name__ == '__main__':
    print('Добро пожаловать в программу Банкомат')
    balance = 0
    count = 1
    flag = True
    while flag:
        balance, flag = menu(balance, count, flag)
        
