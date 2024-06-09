
# Задание 1. Напишите функцию для транспонирования матрицы

# def transpose(matrix):
#     """ Транспонирует матрицу"""
#     new_matrix = []
#     for i in range(len(matrix[0])):
#         new_matrix.append([])
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             new_matrix[j].append(matrix[i][j])
#     return new_matrix 
    

# if __name__ == '__main__':
#     my_matrix = ([1, 2], [3, 4], [5, 6])
#     print(transpose(my_matrix))
    
# Задание 2. Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

# def make_dict(**kwargs):
#     d = {}
#     for k,v in kwargs.items():
#         if hash(k) == True:
#             d[v] = k
#         else:
#             v = str(v)
#             d[v] = k
#     return d


# if __name__ == '__main__':
#      print(make_dict(a = 5, b = 6, c = [8, 9]))
   

# Задание 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

# from decimal import Decimal

# MIN_SUM = 50
# MIN_COMISSION = 30
# MAX_COMISSION = 600
# PERCENT_TO_TAKE = Decimal(0.015)
# BONUS_COUNTER = 3
# BONUS = Decimal(0.03)
# LIMIT_BEFORE_TAX = 5000000
# TAX_RATE = Decimal(0.1)

# def menu(balance: Decimal, count: int, flag: bool):
#     dct = {'1. ': '1. пополнить счет',
#            '2. ': '2. снять со счета',
#            '3. ': '3. выйти из программы'}
    
#     for k,v in dct.items():
#         if k.isdigit():
#             print(f'{k}:{v}')
#         else:
#             print(v)
#     my_list = []   
#     if balance > LIMIT_BEFORE_TAX:
#         balance *= (1 - TAX_RATE)

#     choice = input('Выберите команду:')
#     if choice == '3':
#         flag = False
#         print(f'Баланс счета: {balance}.')
#         return balance, flag
#     elif choice == '1':
#         my_list.append('Операция внесения средств: ')
#         balance = get_money(balance)
#         print(f'{my_list},Баланс счета: {balance}.')
#         count += 1
#     elif choice =='2':
#         balance = give_money(balance)
#         count += 1
#     else:
#         print("Неверная команда")
       
    
#     if count % BONUS_COUNTER == 0:
#         balance *= (1+BONUS)
    
#     return balance, flag
#     print (my_list)

# def get_money(balance: Decimal):
#     money_to_get = Decimal(input("Введите сумму пополнения: "))
   
#     if money_to_get % MIN_SUM == 0:
#         return balance + money_to_get
#     else:
#         print('Ошибка: сумма должна быть кратна 50. ')
#         return balance, flag
    
# def give_money(balance: Decimal):
#     money_to_give = Decimal(input("Введите сумму снятия: "))
        
#     if money_to_give % MIN_SUM == 0:
#         percent = money_to_give * PERCENT_TO_TAKE
        
#         if percent <  MIN_COMISSION:
#             percent = MIN_COMISSION
#         elif percent > MAX_COMISSION:
#             percent = MAX_COMISSION
        
#         if balance < (money_to_give + percent):
#                 print('Сумма снятия с комиссией за услугу больше доступного баланса.')
#         else:
#             balance -= (money_to_give + percent)
#     else:
#         print('Ошибка: сумма должна быть кратна 50. ')
            
#     if count > BONUS_COUNTER:
#         balance += (balance * BONUS)
#     return balance, flag

# if __name__ == '__main__':
#     print('Добро пожаловать в программу Банкомат')
#     balance = int(0)
#     count = 1
#     flag = True
#     while flag:
#         balance, flag = menu(balance, count, flag)


        
