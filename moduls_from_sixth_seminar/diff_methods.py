
from random import randint

def arr_of_queens(queens: list, n: int):
    for i in range(n-1):
        for j in range(i + 1, n):
            if queens[i][0] == queens[j][0] or \
               queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return True
    return False


def counter(s, count = 0):
    while count < 4:
        list_one = list(map(lambda _: randint(1, s+1), range(s)))
        list_two = list(map(lambda _: randint(1, s+1), range(s)))
        queens3 = list(zip(list_one, list_two))
        if arr_of_queens(queens3, s):
            count += 1
            print(queens3)

if __name__=='__main__':
    n = 8
    queens = [[1, 6], [2, 2], [3, 7], [4, 1], [5, 4], [6, 8], [7, 5], [8, 3]]
    if arr_of_queens(queens, n):
        print("YES")
    else:
        print("NO")
    
    counter(n)