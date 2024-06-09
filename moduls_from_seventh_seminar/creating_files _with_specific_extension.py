import os
import random as rd

min_letter = ord('a')
max_letter = ord('z')

def generate_text(length):
    """Генерирует случайны текст определенной длины"""
    name = []
    for i in range(length):
        name.append(chr(rd.randint(min_letter, max_letter)))
    return ''.join(name)

def generate_files(extension: str,
                   directory: str,
                   min_length=6,
                   max_length=30,
                   min_bytes=256,
                   max_bytes=4096,
                   num_files=42):
    """Генерирует файлы с заданными параметрами"""
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    for i in range(num_files):
        name_length = rd.randint(min_length, max_length)
        filename = generate_text(name_length)
        text_length = (rd.randint(min_bytes, max_bytes))
        text = generate_text(text_length)
    while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break

def generate_with_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        generate_files(key,'files', num_files=value)
 

if __name__ == '__main__':
    generate_files('rnd', 'files')
    d = {
        'doc': 5,
        'jpg': 10,
        'png': 23,
        'txt': 15
    }
    generate_with_dictionary(d)
