import json
import os

def create_json_users(name='db.json'):
    """ Запрашивает у пользователя информацию и добавляет ее в json-файл"""
    db = {}
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    with open(name, 'w', encoding='utf-8') as f:
        while True:
            while True:
                try:
                    user_level = int(input('Введите число от 1 до 7 или любую букву для выхода: '))
                except:
                    json.dump(db, f)
                    exit()
                else:
                    break
            if not 1 <= user_level <= 7:
                continue
            if user_level not in db:
                db[user_level] = {}
            while True:
                try:
                    user_id = int(input('Введите идентификатор: '))
                except:
                    print("Вы ввели не число")
                else:
                    flag = False
                    for level in db:
                        for ident in db[level]:
                            if ident == user_id:
                                print("Идентификатор должны быть уникальным.")
                                flag = True
                                break
                    if flag:
                        continue
                    else:
                        break
            while True:
                user_name = input('Введите имя: ')
                if user_name:
                    break
                else:
                    print("Вы не ввели имя")
            db[user_level][user_id] = user_name


if __name__ == '__main__':
    create_json_users()