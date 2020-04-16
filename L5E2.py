
with open('my_file2.txt', 'r') as my_f:
    content = my_f.readlines()
    print(f'Строк в файле - {len(content)}')

with open('my_file2.txt', 'r') as my_f:
    content = my_f.read()
    content = content.split()
    print(f'Общее кол-во слов в файле = {len(content)}')




