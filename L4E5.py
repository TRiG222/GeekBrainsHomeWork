from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(prev_i, i):
    return i * prev_i


print(reduce(my_func, my_list))
