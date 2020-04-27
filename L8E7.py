class Complex:
    def __init__(self, param_1, param_2):
        self.param_2 = param_2
        self.param_1 = param_1

    def __add__(self, other):
        if self.param_2 + other.param_2 == 0:
            return f'Сумма комплексных числе = {self.param_1 + other.param_1}'
        return f'Сумма комплексных числе = {self.param_1 + other.param_1} + {self.param_2 + other.param_2}*j'

    def __mul__(self, other):
        a = self.param_1 * other.param_1
        b = self.param_1 * other.param_2
        c = self.param_2 * other.param_1
        d = -(self.param_2 * other.param_2)
        return f'Произведение комплексных чисел = {a + d} + {b + c}*j'


num_1 = Complex(2, 3)
num_2 = Complex(2, -2)
print(num_1 + num_2)
print(num_1 * num_2)
