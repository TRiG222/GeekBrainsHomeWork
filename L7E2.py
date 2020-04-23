from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, name, size, height):
        self.size = size
        self.height = height
        self.name = name

    def clot_coat(self):
        return print(f'Вот столько ткани нужно для пальто {self.size} размера\n{round(self.size / 6.5 + 0.5, 3)}')

    def clot_costume(self):
        return print(
            f'Cтолько нужно ткани на один костюм рост которого {self.height}\n{round(self.height * 2 + 0.3, 3)}')

    @property
    def full_sq(self):
        return print(f'Общая площадь ткани {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Clothes):

    def __init__(self, name, size, height):
        super().__init__(name, size, height)

    @property
    def clot_coat(self):
        return print(
            f'Вот столько ткани нужно для пальто {self.name} {self.size} размера\n{round(self.size / 6.5 + 0.5, 2)}')


class Costume(Clothes):

    def __init__(self, name, size, height):
        super().__init__(name, size, height)

    @property
    def clot_costume(self):
        return print(
            f'Cтолько нужно ткани на один костюм {self.name} рост которого {self.height}\n'
            f'{round(self.height * 2 + 0.3, 2)}')


Coat_1 = Coat('Versace', 33, 18)
Costume_1 = Costume('Adidas', 33, 18)
Coat_1.clot_coat
Costume_1.clot_costume
Coat_1.full_sq
