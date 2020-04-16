line = input('Введите текст:\n')
with open('my_file1.txt', 'w') as my_f:
    while line:
        my_f.write(line + '\n')
        line = input('Введите текст:\n')
        if not line:
            break







with open('my_file1.txt') as my_f:
    content = my_f.readlines()
    print(content)


