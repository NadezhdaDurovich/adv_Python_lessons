# отдельно в той же папке создаем директорию mathematical c пустым файлом "__init__.py". В ней создаем файл base_math.py и advanced_math.py (наши собственные модули c набором функций )

# from mathematical import base_math # импортируем модуль в рабочий файл

# # запускаем фукции модуля:
# print(base_math.add(2, 3))
# print(base_math.mul(2, 3))

# from mathematical import advanced_math

# print(advanced_math.divi(42, 10))
# print(advanced_math.exp(2, 2))

# Варианты импорта

# import mathematical

# x = mathematical.base_math.div(12, 5)

# from mathematical import base_math as bm
# from mathematical.advanced_math import exp

# x = bm.div(12, 5)
# z = exp(2, 3)

# Модуль из "коробки"
import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(rnd.random())
rnd.seed(42)
state = rnd.getstate()
print(rnd.random())
rnd.setstate(state)
print(rnd.random())

print(rnd.randint(START, STOP)) # генерация случайного целого числа в диапазоне от a включительно до b включительно — [a, b].
print(rnd.uniform(START, STOP)) # генерация случайного вещественного числа в диапазоне от a до b. Правая граница может как входить, так и не входить в возвращаемый диапазон. Зависит от способа округления.
print(rnd.choice(data)) # возвращает случайный элемент из непустой последовательности.
print(rnd.randrange(START, STOP, STEP)) #работает как вложение функции range в функцию choice, т.е. choice(range(start, stop, step)).Возвращает случайное число от start до stop с шагом step.

print(data)
rnd.shuffle(data) #перемешивает случайным образом изменяемую последовательность in place, т.е. не создавая новую.
print(data)

print(rnd.sample(data, 2)) # выбирает k уникальных элементов из последовательности  и возвращает их в новой последовательности.
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100])) #Параметр counts позволяет указать количество повторов элемента.


# Для управления состоянием используют следующие 3 функции:
# ● seed(a=None, version=2) — инициализирует генератор. Если значение a не указано, для инициализации используется текущее время ПК. Версия 2 используется со времён Python 3.2 как основная. Не стоит менять её.
# ● getstate() — возвращает объект с текущим состоянием генератора.
# ● setstate(state) — устанавливает новое состоянии генератора, принимая на # вход объект, возвращаемый функцией getstate.  