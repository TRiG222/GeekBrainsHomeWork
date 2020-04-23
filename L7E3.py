class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат сложения клеток = {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Результат вычитания клеток = {self.quantity - other.quantity}'
        else:
            return f'Операция невозможна'

    def __mul__(self, other):
        return f'Результат произведения клеток = {self.quantity * self.quantity}'

    def __truediv__(self, other):
        if (self.quantity / other.quantity) > 1:
            return f'Результат деления клеток = {int(round((self.quantity / other.quantity), 1))}'
        else:
            return f'Операция невозможна'

    def make_order(self, row_cell):
        row = str()
        for i in range(int(self.quantity / row_cell)):
            row += f'{"*" * row_cell}\n'
        row += f'{"*" * (self.quantity % row_cell)}'
        return row


Cell_1 = Cell(40)
Cell_2 = Cell(9)
print(Cell_1 + Cell_2)
print(Cell_1 - Cell_2)
print(Cell_1 * Cell_2)
print(Cell_1 / Cell_2)

print(Cell_1.make_order(9))
