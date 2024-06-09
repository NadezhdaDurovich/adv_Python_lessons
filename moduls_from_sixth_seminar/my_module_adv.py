
from datetime import datetime as dt
from calendar import isleap

from sys import argv

__all__=['check_date', 'if_is_leap']

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        if_is_leap(t.year)
        return True
    except:
        return False
    
def if_is_leap(year: int):
    print("Високосный" if isleap(year) else "Не високосный")

if __name__=='__main__':
    if len(argv) == 2:
        print(check_date(argv[1]))
    print(check_date(input('Введите дату чч.мм.ггг: ')))
