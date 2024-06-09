
from sys import argv

from random import randint


def quess_number(lower_limit=1, upper_limit=100, attempt=10):
    rand_num = randint(lower_limit, int(upper_limit)+1)
    print(rand_num) # подсказка
    num = None
    print("Компьютер загадал число. Угадайте, какое?")
    while attempt > 0:
        print()
        print(f'У Вас осталось {attempt} попыток: ')
        attempt -=1
        print()
        print("Введите число между числами", lower_limit, 'и', upper_limit, ': ')
        num = int(input())
        if num < lower_limit or num > upper_limit:
            print("Вы не попали в заданный диапазон, попроуйте еще раз.")
        else:
            if num != rand_num:
                print("Не угадали, увы!", end='\t')
                if num < rand_num:
                    print("Загаданное число больше.")
                    print()
                else:
                    print("Загаданное число меньше.")
                    print()
            else: 
                break
    else: 
        print("К сожалению, все попытки закончились.")
        quit() # завершение работы программы

    print(f'Ура! Вы сделали это! Загаданное чисо действительно {rand_num}')


if __name__ == '__main__':
    quess_number(0, 1000, 10)
    print(argv)
    # n = len(argv)
    # match n:
    #     case 1:
    #         lower_limit = 0
    #         upper_limit = 100
    #         attempt = 10
    #     case 2:
    #         lower_limit = int(argv[1])
    #         upper_limit = 100
    #         attepmt = 10
    #     case 3:
    #         lower_limit = int(argv[1])
    #         upper_limit = int(argv[2])
    #         attepmt = 10
    #     case _:
    #         lower_limit = int(argv[1])
    #         upper_limit = int(argv[2])
    #         attepmt = int(argv[3])
    # # print(lower_limit, upper_limit,  attepmt)
    # quess_number(*argv[1:])