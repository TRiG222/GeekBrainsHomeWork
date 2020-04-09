def my_func(arg_1, arg_2, arg_3):
    num = arg_1, arg_2, arg_3
    num = sorted(num)  # сортировка списка по возрастанию(правильно ли было решать через сортировку?)
    return print(sum(num[-1:0:-1]))  # сумма среза двух больших чисел


my_func(arg_1=int(input('Введите первое число: ')),
        arg_2=int(input('Введите второе число: ')),
        arg_3=int(input('Введите третье число: ')))
