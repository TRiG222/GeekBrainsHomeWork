def div(arg_1, arg_2):
    try:
        return print(round(arg_1 / arg_2, 2))  # деление и округление
    except ZeroDivisionError:  # обработка деления на ноль
        print('На ноль делить нельзя!')



div(arg_1=int(input('Введите первое число: ')),
    arg_2=int(input('Введите второе число: ')))  # ввод аргументов
