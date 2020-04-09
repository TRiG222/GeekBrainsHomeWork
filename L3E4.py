"""
Первый вариант решения с  " ** "
"""


def exponentiation(x, y):
    try:
        if not y < 0 and x(type(float)):  # проверка на формат чисел
            raise Exception()
        print(x ** y)
    except Exception:
        print('Неверный формат ввода')


exponentiation(x=float(input('Введите действительное положительное число: ')),
               y=int(input('Введите целое отрицательное число: ')))

"""
Второй вариант решения с циклом
"""


def cycle(a, b):
    try:
        if not a(type(float)) and b < 0:
            raise Exception()
        i = 1
        while b < 0:
            i = i / a
            b += 1
        print(i)
    except Exception:
        print('Неверный формат ввода')




cycle(a=float(input('Введите действительное положительное число: ')),
      b=int(input('Введите целое отрицательное число: ')))
