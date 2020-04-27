class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_f(num_1, num_2):
    try:
        if num_2 == 0:
            raise OwnError('Ошибка!Мы не можем поделить на ноль')
        else:
            print(num_1 / num_2)
    except OwnError as my_err:
        print(my_err)
        return my_f(num_1=int(input('Введите делимое число: ')), num_2=int(input('Введите делитель: ')))


my_f(num_1=int(input('Введите делимое число: ')), num_2=int(input('Введите делитель: ')))
