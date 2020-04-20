class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print('Идет расчет . . .')

    def mass(self):
        self.weight = 25
        self.thickness = 0.05
        mass = self._length * self._width * self.weight * self.thickness / 10
        print(f'Нужно {int(mass)}т. асфальта')


Road = Road(40, 50000)
Road.mass()
