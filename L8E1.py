import re


class Data:
    def __init__(self, param):
        self.param = param

    @classmethod
    def num_1(cls, param):
        date = []
        for i in re.split(r'-', param):
            date.append(int(i))
        return date

    @staticmethod
    def num_2(date):
        if date[0] < 1 or date[0] > 31:
            print('Не верное значение')
        elif date[1] < 1 or date[1] > 12:
            print('Не верное значение')
        elif date[2] < 0:
            print('Не верное значение')
        else:
            return f'Введеная вами дата {date} верна.'






print(Data.num_2(Data.num_1('20-12-2020')))
