from math import factorial


def fact(n):
    if n == 1:
        gen = [1]
    else:
        gen = [factorial(n) for n in range(2, n + 1)]
    yield gen


_ = 0
for el in fact(int(input('Введите число из которого будем искать факториал: '))):

    if _ < 15:
        print(f'Факториал числа равен: {el}')
        _ += 1
    else:
        break
