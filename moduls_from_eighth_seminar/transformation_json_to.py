import json
import os
import pickle

def json_to_csv(name='db.json', res_file='db.csv'):
    """сохраняет json файл в формате CSV"""
    with open (name,'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    with open(res_file, 'w', encoding='utf-8') as f_csv:
        for k, v in db.items():
            for k2, v2 in v.items():
                print(f'{k},{k2},{v2}', file = f_csv)
       

def json_to_pickle(directory='.'):
    """Ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов."""
    for file in os.listdir(directory):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.json':
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                data =json.load(f)
            with open(os.path.join(directory, file_name + '.pickle'), 'wb') as f:
                pickle.dump(data, f)



if __name__ == '__main__':
    json_to_csv()
    json_to_pickle()


