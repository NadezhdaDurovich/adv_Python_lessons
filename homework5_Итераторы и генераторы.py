# Задание 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# import os

# def file_info(file_path):
#     path, filename = os.path.split(file_path)
#     name, extension = os.path.splitext(filename)
#     return path, name, extension

# path_to_file = os.path.join(os.getcwd(), 'dir', 'task_1.py')

# print(file_info(path_to_file))    



# Задание 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.

# surnames = ['Иванов', 'Петров', 'Сидоров']
# salaries = [60_000, 75_000, 85_000]
# rates = ['10.25%', '10.25%', '10.25%']

# bonuses = {surname: salary*float(rate[:-1])/100 for surname, salary, rate in zip(surnames, salaries, rates)}

# print(bonuses)


# Задание 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# N = int(input('Enter N Number: '))

# def list_fib():
#     old, new = 0, 1
#     while True:
#         yield old
#         old, new = new, old + new

# generate_fibonachi = list_fib()
# for i in range (N+1):
#     print(next(generate_fibonachi), end =' ')