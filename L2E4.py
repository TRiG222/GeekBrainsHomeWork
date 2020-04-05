my_str = input('Введите слова через пробел ')
my_str = my_str.split()
num = 1
print(my_str)
for i in my_str:
    if len(i) > 10:
        print(f'{num}.{i[0:10]}')
        num += 1
    else:
        print(f'{num}.{i}')
        num += 1
