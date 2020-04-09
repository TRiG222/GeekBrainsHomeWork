i = 0  # переменная сохраняющая сумму

print('Для выхода из программы введите  "q"')


def my_func(my_list):  # функция превращения ввода в формат int
    global i
    result = [int(item) for item in my_list]
    sum_count = sum(result)
    i = i + sum_count
    print(f'Сумма чисел равна:{i}')


def count(a):
    global i
    my_list = a.split()
    if 'q' in my_list:  # условие выхода из программы
        my_list.remove('q')  # счет если введены числа и спец символ
        my_func(my_list)
        return print('Программа завершена')
    else:
        my_func(my_list)
        return count(a=input('Введите числа через пробел и нажмите Enter: '))


count(a=input('Введите числа через пробел и нажмите Enter: '))
