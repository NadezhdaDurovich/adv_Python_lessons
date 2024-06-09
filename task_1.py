# Переменные, их имена и место в памяти

#name = 'Nadezhda'
#age = None
#a = 41
#print(id(a))
#a =  'Hello,world!'
#print(id(a))
#a =  3.14 / 3
#print(id(a))

#print (name, age, a, 456, 'Hello', sep=';', end='\n')
#print ('Any text')

# Работа с данными от пользователя

#res = input('print your text: ')
#print ('You wrote', res)

# Заменяем "магические" числа на константы!

#ADULT = 18
#age = int(input('How old are you ? '))

#how_old = age-ADULT
#print (how_old, 'лет назад ты стал совершеннолетним')


# Конструкции ветвления if,elif,else,match, case

"""pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Access is allowed')
    my_math = int(input('2+2 = '))
    if 2+2 == my_math:
        print ("It's a real world")
    else:
        print("It's a matrix")
else:
    print('access denied')"""

#color = input("What's your favorite color? ")
"""if color == 'red':
    print('Wow, you are a lover of bright!')
elif color == 'green':
    print('Are you by any chance a hunter?;)')
elif color == 'blue':
    print('Yea, classic!')
else:
    print("Ugh, that's a strange choice")"""
"""match color:
    case 'red' | 'orange':
        print('Wow, you are a lover of bright!')
    case 'green':
        print('Are you by any chance a hunter?;)')
    case 'blue':
        print('Yea, classic!')
    case _:
        print("Ugh, that's a strange choice")"""
# print('Хочешь я по номеру года скажу, високосный был год или нет?')
#year = int(input('Введи год в форматe yyyy: '))
# Вариант 1 - сложный и долгий
"""if year % 4 != 0:
    print('Это обычный год')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Это високосный год')
    else:
        print('Это обычный год')
else:
    print('Это високосный год')"""
# Вариант 2 - простой и быстрый
"""if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('Это обычный год')
else:
     print('Это високосный год')"""

"""data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num  = int(input('Введите любое число: '))
if num in data:
    print("Matched!")
else:
    print("Try again")"""

# Обычная конструкция ветвления:

# my_math = int(input('2+2 = '))
"""if 2+2 == my_math:
    print ("Верно!")
else:
    print("Вы уверены?")"""

#Тернарный оператор python сокращает запись кода:

# print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')

# Циклы while

# continue переносит действия сразу к началу цикла
#num = float(input("Введите число: "))
#count = 0
#while count < num:
#    print(count)
#    count += 2
""" STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue
    print(count)"""

"""min_limit = 0
max_limit = 10
while True: # бесконечный цикл
    print("Введите число между", min_limit, 'и', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else: 
        break # используем для остановки бесконечного цикла
print("Было введено число", num)"""

"""min_limit = 0
max_limit = 10
count = 3
num = None

while count > 0:
    print('Осталось попыток: ', count)
    count -=1
    
    print("Введите число между", min_limit, 'и', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else: 
        break

else:
    print("Исчерпаны все попытки, сожалеем.")
    quit() # завершение работы программы

print('Было введено число ', num)"""

# Разберем цикл for in

"""data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)"""

"""num = int(input("Введите число: "))
for i in range(0, num, 2):
    print(i)"""

#animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']

#for i, animal in enumerate (animals, start=1):
#    print(i, animal)

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)

