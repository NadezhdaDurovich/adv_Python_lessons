# Задание 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c — стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
# a = int(input("Введите длину первой стороны треугольника: "))
# b = int(input("Введите длину второй стороны треугольника: "))
# c = int(input("Введите длину третьей стороны треугольника: "))

# if a > (b + c) or b > (a + c) or c > (a + b):
#     print(f"треугольника со сторонами ({a, b, c}) не существует")
# else:
#     if a == b == c:
#         print(f"треугольник со сторонами ({a, b, c}) равносторонним")
#     elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2): 
#         print(f"треугольник со сторонами ({a, b, c}) прямоугольный")
#     elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
#         print(f"треугольник со сторонами ({a, b, c}) равнобедренный")
#     else:
#         print(f"треугольник со сторонами ({a, b, c}) разносторонний")
    

# Задание 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: «Число является простым, 
# если делится нацело только на единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# MIN_NUM = 0
# MAX_NUM = 100000
# status='simple'
# number = int(input('Enter any number in the range [0, 100001): '))
# if (number < MIN_NUM) or (number > MAX_NUM):
#     print("Oops, you didn't get into the set range, please try again")
# else:
#     for i in range(2, (number//2)+1):
#         if number % i == 0:
#             status='not simple'
#     print(f'The number {number} is {status}')


# Задание 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:

# from random import randint

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# rand_num = randint(LOWER_LIMIT, UPPER_LIMIT+1)
# print(rand_num)
# attempt = 10
# num = None

# while attempt > 0:
#     print()
#     print(f'There are {attempt} attempts left')
#     attempt -=1
#     print()
#     print("Enter any number between", LOWER_LIMIT, 'and', UPPER_LIMIT, ': ')
#     num = int(input())
#     if num < LOWER_LIMIT or num > UPPER_LIMIT:
#         print("Oops, you didn't get into the set range, please try again")
#     else:
#         if num != rand_num:
#             print("You didn't guess right.", end='\t')
#             if num < rand_num:
#                 print("The hidden number is bigger.")
#                 print()
#             else:
#                 print("The hidden number is smaller.")
#                 print()
#         else: 
#             break
# else:
#     print("Unfortunately, all attempts were used.")
#     quit() # завершение работы программы

# print(f'Hooray, you did it! The number {num} was guessed ')


