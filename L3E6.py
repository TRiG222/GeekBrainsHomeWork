"""
В этом задании не понял, что от меня требуется во второй части задания
"""

latin = set('qwertyuioplkjhgfdsazxcvbnm ') # список проверки на латынь и нижний регистр


def int_func(a):
    for i in a:
        if i not in latin:
            return print('Можно вводить только латинские буквы в нижнем регистре!')
    print(a.title())


int_func(a=input('Введите слово латинскими буквами и в нижнем ригистре: '))


def title_all(b):
    my_list = b
    int_func(my_list)


title_all(b=input('Введите слова латинскими буквами и в нижнем ригистре через пробел: '))
