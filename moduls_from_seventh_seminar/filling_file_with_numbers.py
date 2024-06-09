import os
import random as rd

left = -1000
right = 1000

def generate_number_into_file(count: int, filename: str):
    """Заполняет файл случайными парами чисел рандомно сгенерированных в заданном диапазоне"""
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{rd.randint(left, right)} | {rd.random() * 2000 - 1000}')
            f.write('\n' if i < count - 1 else ' ')

if __name__ == '__main__':
    rows = 10
    generate_number_into_file (rows, 'new_data.txt')