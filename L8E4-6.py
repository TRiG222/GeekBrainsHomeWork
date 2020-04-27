class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:  # класс склада
    def __init__(self):

        self.total = {}  # все что хранится на складе
        self.dep_1 = []  # отдел менеджмента
        self.dep_2 = []  # бухгалтерия

    def income_warehouse(self):  # внесение техники на склад
        keys = []
        values = []
        i = 0
        print('Введите "q" для завершения ввода')
        while i == 0:
            try:
                name = input('Введите наименование: ').lower()
                if name != 'q':
                    quantity = int(input('Введите кол-во: '))
                    keys.append(name)
                    values.append(quantity)
                elif name == 'q':
                    i += 1
            except ValueError:
                print('В строке кол-во должно быть введено число')
        g = (list(zip(keys, values)))
        d = dict(enumerate(g, 1))
        self.total.update(d)
        print(f'Ввод позиций завершен!')

    def move_to_dep(self): # перемещение склад ===> отдел
        try:
            num_dep = int(
                input('Введите номер отдела в который хотите перенести позицию\n1.Менеджмент\n2.Бухгалтерия\n'))
            if num_dep == 1:
                for key, value in self.total.items():
                    print(key, ":", value)
                num = int(input(f'Введите номер позиции которую хотите переместить: '))
                _ = self.total.get(num)
                self.dep_1.append(_)
                self.total.pop(num)
                print(f'Список техники в отделе Менеджмента: {self.dep_1}')
            elif num_dep == 2:
                for key, value in self.total.items():
                    print(key, ":", value)
                num = int(input(f'Введите номер позиции которую хотите переместить: '))
                _ = self.total.get(num)
                self.dep_2.append(_)
                self.total.pop(num)
                print(f'Список техники в отделе Менеджмента: {self.dep_2}')

            else:
                raise OwnError('Введенного отдела не существует')
        except OwnError as err:
            print(err)
            return w_1.move_to_dep()


class Equipment:  # класс техники
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Printer(Equipment):
    def to_print(self):
        return f'Start printing . . .'


class Scanner(Equipment):
    def to_scan(self):
        return f'Start scanning . . .'


class Xerox(Equipment):
    def to_copy(self):
        return f'Start copying . . .'


w_1 = Warehouse()
w_1.income_warehouse()
w_1.move_to_dep()

