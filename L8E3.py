class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_l = list()


def my_f(num):
    try:
        a = any(map(str.isdigit, num))
        if a is False:
            if num == 'q':
                print(f'Вот список с нашими числами {my_l}')
            else:
                raise OwnError('Ошибка!Ввод не является числом.')


        elif a is True:
            my_l.append(num)
            return my_f(num=input('Введите число: '))

    except OwnError as my_err:
        print(my_err)
        return my_f(num=input('Введите число: '))


my_f(num=input('Для завершения программы введите "q"\nВведите число: '))
