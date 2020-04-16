with open('text_3.txt', 'r') as my_f:
    less = []
    average = []
    my_list = my_f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000.0:
            less.append(i[0])
        average.append(i[1])
print(f'Оклад менее 20к - {less}\nCредний оклад = {sum(map(float,average)) / len(average)}')
