import os

def read_line_or_begin(fd) -> str:
    """Начинает снова читать файл с первой строки, когда файл уже прочитан"""
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]

def process_files(file_numbers, file_names, file_res):
    """Создает новый файл из двух существующих (с заданными параметрами0"""
    with open(file_numbers, 'r', encoding='utf-8') as f_num:
        with open(file_names, 'r', encoding='utf-8') as f_nam:
            with open(file_res, 'w', encoding='utf-8') as f_res:
                length1 = len(f_num.readlines())
                length2 = len(f_nam.readlines())
                length = max(length1, length2)
                for i in range(length):
                    line_num = read_line_or_begin(f_num)
                    line_nam = read_line_or_begin(f_nam)
                    a, b  = line_num.split('|')
                    a = int(a)
                    b = float(b)
                    res = a * b
                    if res < 0:
                        res *= -1
                        line_nam = line_nam.lower()
                    else:
                        res = round(res)
                        line_nam = line_nam.upper()
                    f_res.write(f'{line_nam} {res}')
                    f_res.write('\n' if i < length - 1 else ' ')


if __name__ == '__main__':
    process_files('new_data.txt', 'data.txt', 'res.txt')
