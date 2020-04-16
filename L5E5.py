from random import randint

with open('file_5.txt', 'w+') as my_f:
    line = [randint(1, 10) for i in range(10)]
    my_f.writelines(str(line))
    print(f'Сумма числе в файле = {sum(map(int, line))}')
