# Урок 4. Функции

# Задание 1. 

# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки. Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode. Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# def print_text(text: str):
#     """Функция принимает строку текста и выводит каждое слово с новой строки"""
#     text_1st = text.split()
#     text_1st.sort()
#     max_len = max(len(word) for word in text_1st)    
#     #max_len1 = len(max(text_1st, key=len))
#     for i, word in enumerate(text_1st, 1):
#         print(f'{i}  {word:>{max_len}}')
    

# if __name__ == '__main__':
#   print_text(input("Введите свой текст: "))
    
# Задание 2. 

# Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

# def text_unicode(text: str) -> list:
#   """ Возвращает отсортированный по убыванию список с уникальными кодами Unicode """
#   return list(map(ord, sorted(set(text), reverse=True))) # функция ord возвращает код unicode от символа, reverse=True - сортировка по убыванию


# if __name__ == '__main__':
#   print(text_unicode(input("Введите строку: ")))

# Задание 3.

# Функция получает на вход строку из двух чисел через пробел. Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

# def unicode_range(text: str) -> dict:
#     """ Возвращает словрь символов.
#     Диапазон пар "ключ-значение" от наименьшего из введённых пользователем чисел до наибольшего (включительно).
#     """
#     a,b = sorted([int(i) for i in text.split()])
#     return {chr(i):i for i in range(a,b+1)}

# if __name__ == '__main__':
#   text = input("Введите два числа: ")
#   print(unicode_range(text))

# Задание 4. 
# Функция получает на вход список чисел. Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
# Как вариант, напишите сортировку пузырьком. Eё описание есть в википедии.

# def sorted_list(list_of_numbers:list) -> None:
#     """ Сортирует числа в списке на месте"""  
#     for _ in range(len(list_of_numbers)):
#       for j in range(len(list_of_numbers)-1):
#         if list_of_numbers[j]>list_of_numbers[j+1]:
#            list_of_numbers[j],list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
  

# if __name__ == '__main__':
#   num_list = [int(i) for i in input("Введите несколько чисел: ").split()]
#   sorted_list(num_list)
#   print(num_list)

# Задание 5.

#  Функция принимает на вход три списка одинаковой длины (имена str, з/п ставка int, % премии str) с указанием процентов вида «10.25%».
#  Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии. 

# def calc_bonus(names: list[str], salaries: list[int], percents: list[str])  -> dict[float]:
#     """ Расчет премии.
#         Возвращает словарь с именем в качестве ключа и суммой премии в качестве значения.
#     """
#     bonuses = {}
#     for name, salary, percent in zip(names, salaries, percents):
#       percent = float(percent[:-1])
#       bonuses[name] = salary * percent/100
#     return bonuses


# if __name__ == '__main__':
#   surnames = ['Иванов', 'Петров', 'Сидоров']
#   salaries = [60_000, 75_000, 85_000]
#   rates = ['10.25%', '10.25%', '10.25%']
#   print(calc_bonus(surnames, salaries, rates))

#  Задание 6.

#  Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между переданными индексами.  
#  Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

# def sum_range(numbers: list, a: int, b: int) -> int:
#     """ Вычисляет сумму числел в диапазоне, заданном индексами"""
#     if a > b:
#       a,b = b,a
#     if a < 0:
#       a = 0
#     if b >= len(numbers):
#       b = len(numbers)-1
#     return sum(numbers[a:b+1])


# if __name__ == '__main__':
#   array_numbers = [4, 5, 45, 78, 478, 145]
#   left = 4
#   right = 1
#   print(sum_range(array_numbers, left, right))  

# Задание 7.

# Функция получает на вход словарь с названием компаний в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения. 
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# def all_frofitable(profits: dict) -> bool:
#     """ Подсчет убыточности"""
#     income = [sum(value) > 0 for value in profits.values() ] # формируем список из сумм значений словаря), сравниваем каждую сумму с нулем
#     return all(income) # если все элементы получившего ся списка больще нуля(True), то функция all вернет True


# if __name__ == '__main__':
#   companies_results = {'HP': [600,500,-400], 'HBS': [900,-800,200], 'ABS': [400, -200, 300]} 
#   if all_frofitable(companies_results) == True:
#     print("Все компании прибыльные")
#   else:
#     print("Не все компании прибыльные")

# Задание 8.

# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


# def no_s():
#   """ Удаляет s из окончания имен переменных"""
#   lst = {}
#   for var, val in globals().items():
#     if var != 's' and  var != 'no_s' and var.endswith('s'):
#       lst[var[:-1]] = val
#       globals()[var] = None
#   for k,v in lst.items():
#     globals()[k] = v
  

# if __name__ == '__main__':
#   items = 0
#   names = 'ghj'
#   s = 5
#   value ='zxc'
#   print(globals())
#   no_s()
#   print(globals())