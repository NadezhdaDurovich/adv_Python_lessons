import os
import random as rd

vowels = {'a', 'y', 'o', 'u', 'i', 'e'}
max_len = 7
min_len = 4
min_letter = ord('a')
max_letter = ord('z')

def generate_names_file(filename: str, count: int):
    """Генерирует псевдоимена определенной длины"""
    with open (filename, 'w', encoding='utf-8') as f:
        for j in range (count):
            len_name = rd.randint (min_len, max_len)
            name = []
            for i in range (len_name):
                name.append(chr(rd.randint(min_letter, max_letter)))
            has_vowels = False
            for letter in name:
                if letter in vowels:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = rd.randint(0, len_name - 1)
                letter = rd.choice(list(vowels))
                name[ind] = letter
            print(''.join(name). capitalize(), file=f, end ='')
            f.write('\n' if i < count    - 1 else ' ')

if __name__ == '__main__':
    count = 25   
    generate_names_file('data.txt', count)