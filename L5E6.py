"""
На решение этой задачи у меня ушло очень и очень много часов
Решено благодаря информации в гугле + большого кол-ва дебажиния)
"""

import re


data = [] #переменная с суммой часов
subj = {} # словарь

def my_f(): # функция для получения чисел и суммирования
    with open('text_6.txt', 'r') as file:

        values = file.read().split('\n')
        for key in values:
            values = re.findall(r'[-+]?\d*\.\d+|\d+', key)
            if values != []:
                global a
                a = sum(map(int, values))
                data.append(a)


def subject_f(): #функция для получение предмета и формирование словаря
    with open('text_6.txt', 'r') as file:
        my_f()
        i = -1
        for line in file:
            subject = line.split(' ')

            print(f'{subject[0]} = {data[i + 1]} часов')
            global subj
            subj[subject[0]]=data[i + 1]
            i += 1


subject_f()
print(subj)
