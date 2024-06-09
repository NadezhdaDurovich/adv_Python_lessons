
import json

def text_to_json(name = 'res.txt'):
    """Cоздаёт из текстового файла новый файл с данными в формате JSON"""
    with open (name, 'r', encoding='utf-8') as f,\
    open ('result.json', 'a', encoding='utf-8') as f2:
        my_list = []
        for line in f:
            my_list.append(line.capitalize())
        json.dump(my_list, f2, indent=4)


if __name__ == '__main__':
    text_to_json()

