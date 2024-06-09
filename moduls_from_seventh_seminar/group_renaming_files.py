import os
from pathlib import Path

def rename_files(directory: int,
                 new_name_end: str,
                 len_number: int,
                 extnsn_init: str,
                 extnsn_fin: str,
                 curr_name_range: range = (0, 4),
                 ):
    """Групповое переименование файлов по заданным параметрам"""
    count = 1
    if  not os.path.exists(directory) or not os.path.isdir(directory):
            os.mkdir(directory) 
    for file in os.listdir(directory):
          if file.endswith(extnsn_init):
                curr_name = os.path.splitext(file)[0][curr_name_range[0]:curr_name_range[1]]
                new_name = f'{curr_name}{new_name_end}{str(count).zfill(len_number)}{extnsn_fin}'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                count += 1
            

    if __name__ == '__main__':
          rename_files('files', '_new_', 3, 'jpg', 'png')