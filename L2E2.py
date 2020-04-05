value_count = int(input('Введите количество значений списка '))
my_list = []


i = 0
value = 0

while i < value_count:
    my_list.append(input('Введите одно значение списка '))
    i += 1

for j in range(int(len(my_list) / 2)):
    my_list[value], my_list[value + 1] = my_list[value + 1], my_list[value]
    value += 2
print(my_list)
