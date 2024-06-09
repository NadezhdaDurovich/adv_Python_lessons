import pickle
import csv
from pathlib import Path

def csv_to_pickle(file: Path) -> None:
    """ читает csv-файл, дополняет и сохраняет данные в json-файл """
    pickle_list = []
    with open(file, 'r',  encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict ={k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv_to_pickle(Path('db.csv')) 