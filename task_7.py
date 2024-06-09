# Работа с файлами

# open(file[, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None])

# mode - режим работы с файлом
# buffering - определяет режим буферизации.Число больше единицы определяет размер буфера в байтах для двоичных файлов
# encoding - кодировка текста
# errors  - используется только в текстовом режиме и определяет поведение в случае ошибок кодирования или декодирования. 
# newline — отвечает за преобразование окончания строки
# closefd — указывает? оставлять ли файловый дескриптор открытым при закрытии файла
# opener — позволяет передать пользовательскую функцию для открытия файла


# f = open('text_data.txt', encoding='utf-8')
# print(f)
# print(list(f))

# Режимы работы с файлами
# ➢ 'r' — открыть для чтения (по умолчанию)
# ➢ 'w' — открыть для записи, предварительно очистив файл
# ➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
# ➢ 'a' — открыть для записи в конец файла, если он существует
# ➢ 'b' — двоичный режим
# ➢ 't' — текстовый режим (по умолчанию)
# ➢ '+' — открыты для обновления (чтение и запись)


# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write("Окончание файла\n")
# f.close() # обязательно закрывать файл

# f = open('bin_data', 'wb', buffering=64)
# f.write(b'X' * 1200)
# f.close()

# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()

# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# f.close()

# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()

# Менеджер контекста with open

# with open('text_data.txt', 'r+', encoding='utf-8') as f:
#     print(list(f))
# print(f.write('Пока')) # ValueError: I/O operation on closed file.

# with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
#         open('bin_data', 'rb') as f2, \
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# Современный вариант открытия файлов (они автоматом закроются после отработки with):
# with (
#         open('text_data.txt', 'r+', encoding='utf-8') as f1,
#         open('bin_data', 'rb') as f2,
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
# ):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# ● Чтение в список (Медленная по времени и затратная по памяти операция)
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     print(list(f))

# ● Чтение методом read
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     res = f.read()
#     print(f'Читаем первый раз\n{res}')
#     res = f.read()
#     print(f'Читаем второй раз\n{res}')

# При чтении файла блоками фиксированного размера можно воспользоваться циклом while. 
# Дочитав до конца в переменную попадёт пустая строка, которая в цикле будет интерпретирована как ложь и завершит тело цикла.
# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.read(SIZE):
#         print(res)

# ● Чтение методом readline (для чтения текстового файла построчно)
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline():
#         print(res)

# ● Чтение циклом for (Вместо метода readline без аргумента - более короткая запись)
# Файл построчно попадает в переменную line. А для того чтобы избавиться от пустых строк отключили перенос строки в функции print.
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# Если вам необходимо обработать строку без переносов, можно использовать срезы line[:-1] или метод замены line.replace('\n', '')
# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         print(line.replace('\n', ''))   

# Запись и добавление в файл

#● Запись методом write (Метод не добавляет символ перехода на новую строку)
# text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
#     print(f'{res = }\n{len(text) = }')

#Если каждая строка должна сохранятся в файле с новой строки, необходимо самостоятельно добавить символ переноса - \n
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?',]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res = }\n{len(line) = }')

# #● Запись методом writelines (В отличии от write этот метод ничего не возвращает.writelines не добавляет переноса между элементами последовательности.)
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     f.writelines('\n'.join(text)) #чтобы каждый элемент списка text сохранялся в файле с новой строки воспользовались строковым методом join

# ● print в файл (по умолчанию выводит информацию в поток вывода. Обычно это консоль. Но можно явно передать файловый объект для печати в файл)
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?',]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, file=f)
# # функция print добавляет перенос строки.Кроме того ничто не мешает явно изменить параметр end функции:
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?',]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, end='***\n##', file=f)

# Методы перемещения в файле

# ● Метод tell (возвращает текущую позицию в файле. Метод используют для определения в каком месте файла будет произведены чтение или запись
# Действия напоминают движение курсора в строке стрелками влево и вправо.

# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?',]
# with open('new_data.txt', 'w', encoding='utf-8') as f:
#     print(f.tell())
#     for line in text:
#         f.write(f'{line}\n')
#         print(f.tell())
#     print(f.tell())
# print(f.tell()) # ValueError: I/O operation on closed file.

# ● Метод seek позволяет изменить положение “курсора” в файле. Метод возвращает новую позицию “курсора”
# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -способ выбора опорной точки.
# ● whence = 0 - отсчёт от начала файла
# ● whence = 1 - отсчёт от текущей позиции в файле
# ● whence = 2 - отсчёт от конца файла
# Исключение: seek(0, 2) для перехода в конец текстового файла.

# last = before = 0
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?',]
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f'{last = }, {before = }')
#     print(f'{f.seek(before, 0) = }')
#     f.write('\n'.join(text))

# В примере выше мы открыли текстовый файл для одновременного чтения и записи. Переменные last и before хранят позиции двух последних прочитанных строк.
# Дочитав файл в цикле while до конца, изменяем позицию “курсора” на начало последней строки и начинаем запись. Таким образом мы сохранили все строки
# файла, кроме последней, и записали новый текст в конец.

# ● Метод truncate
# truncate(size=None) — метод изменяет размер файла. Метод возвращает позицию после изменения файла

# last = before = 0
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f.seek(before, 0))
#     print(f.truncate()) # метод вырезает текст по текущей позиции курсора

# Если не передать значение в параметр size, будет удалена часть файла от текущей позиции до конца. 
# Если передать параметр size, метод изменяет размер файла до указанного числа символов или байт от начала файла.
# Если size меньше размера файла, происходит усечение файла. 
# Если size большеразмера файла, он увеличивается до указанного размера.
# size = 64
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     print(f.truncate(size))

# Работа с каталогами 
# Текущий каталог
# import os
# from pathlib import Path

# print(os.getcwd()) # текущий каталог
# print(Path.cwd())

# os.chdir('../..') # сменить директорию - перейти на 1 каталог выше

# ● Создание каталогов

# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir() # создаёт каталог в текущей директории

# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
# Path('some_dir/dir/new_path_dir').mkdir(parents=True) #  несколько вложенных друг в друга каталогов


# ● Удаление каталогов
# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

# Важно! Удалить можно лишь пустой каталог. Если внутри удаляемого каталога есть другие каталоги или файлы, возникнет ошибка OSError.

# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и файлы), подойдёт функция из модуля shutil
import shutil
shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')

# ● Формирование пути
import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}') #— путь до файла new_file.txt в каталоге dir текущего каталога.

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
      
# Чтение данных о каталогах)
import os
from pathlib import Path
print(os.listdir()) # Функция listdir возвращает список файлов и каталогов.
p = Path(Path().cwd())
for obj in p.iterdir(): #Метод iterdir у экземпляра класса Path является генератором. В цикле он возвращает объекты из выбранной директории.
    print(obj)
 
# ● Проверка на директорию, файл и ссылку
import os
from pathlib import Path
dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')
p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')

# ● Обход папок через os.walk()

import os
for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')    
# Функция возвращает кортеж из трёх значений:
# ➢ dir_path — абсолютный путь до каталога
# ➢ dir_names — список с названиями всех каталогов, находящихся в dir_path
# ➢ dir_names — список с названиями всех файлов, находящихся в dir_path

#Работа с файлами

#● Переименование файлов
os.rename('old_name.py', 'new_name.py') 
p = Path('old_file.py')
p.rename('new_file.py')
Path('new_file.py').rename('newest_file.py')

# ● Перемещение файлов
os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

#● Копирование файлов
import shutil
shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')

# Если стоит задача скопировать каталог со всем его содержимым в новое место, модуль предоставляет функции copytree
shutil.copytree('dir', 'one_more_dir')

#● Удаление файлов
shutil.rmtree('dir') # удаление всего каталога целиком с содержимым

os.remove('one_more_dir/one.txt') # удалить один файл
Path('one_more_dir/one_more.txt').unlink()