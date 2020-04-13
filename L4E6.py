from itertools import count
from itertools import cycle


def count_func(start_n,stop_n):
    for el in count(start_n):
        if el > stop_n:
            break
        else:
            print(el)


count_func(start_n=int(input('Введите начальное число: ')),stop_n=int(input('Введите конечное число: ')))


def cycle_func(start_n, stop_n):
    i = 0
    for el in cycle(start_n):
        if i > stop_n:
            break
        else:
            print(el)
            i += 1


cycle_func(start_n=(input('Введите значение: ')),stop_n=int(input('Введите кол-во циклов: ')))



