import os


new_dict = {'doc': 'texts', 'txt': 'texts', 'jpg': 'pictures', 'png': 'pictures'}

def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.rsplit('.')[:-1]
        if extension not in new_dict:
            continue
        new_directory = f'{directory}/{new_dict[extension]}'
        if  not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.mkdir(new_directory) 
        os.rename(f'{directory}/{f}',
                  f'{new_directory}/{f}')
        

if __name__ == '__main__':
    sort_files('files')
