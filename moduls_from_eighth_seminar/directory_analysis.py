
import os
from pathlib import Path
import json
import pickle
import csv
from transformation_txt2json import text_to_json
from transformation_json_to import json_to_csv
from transformation_csv2pickle import csv_to_pickle

def analysis_directory_results(directory):
    """Cохраняет данныe по результату обхода директории в файлы формата json, csv и pickle """
    files_list=['Файлы: ',]
    directories_list=['Директории: ',]
    for obj in directory:
        if os.path.isfile(obj):
            files_list.append(obj)
            files_list.append(os.path.getsize(obj))  
            files_list.append(os.path.abspath(obj))
        else:
            directories_list.append(obj)
            directories_list.append(os.path.getsize(obj))  
            directories_list.append(os.path.abspath(obj))  

    with open('files_analysis_data.txt', 'w', encoding='utf-8') as f_fil:
        f_fil.write((str(files_list)))

    text_to_json('files_analysis_data.txt')
    json_to_csv('result.json','result.csv')
    csv_to_pickle(Path('result.csv'))

    with open('directories_analysis_data.txt', 'a', encoding='utf-8') as f_dir:
        f_dir.write((str(directories_list)))
    text_to_json('directories_analysis_data.txt')
    json_to_csv('result.json','result.csv')
    csv_to_pickle(Path('result.csv'))
    
    
if __name__=='__main__':
    analysis_directory_results('files')
       




