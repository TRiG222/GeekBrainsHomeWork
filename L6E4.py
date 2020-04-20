from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'{self.name} начинает движение')

    def stop(self):
        print(f'{self.name} останавливается')

    def turn(self):
        i = randint(1, 2)
        if i == 1:
            print(f'{self.name} поворачивает налево')
        else:
            print(f'{self.name} поворачивает направо')

    def show_speed(self):
        return print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} Ваша скорость {self.speed}')
        if self.speed > 60:
            print(f'{self.name} Вы превысили скорость!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')
        if self.speed > 40:
            print('Вы превысили скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не полицейская машина')


auto_1 = SportCar(120, 'black', 'bmw', False)
auto_2 = TownCar(100, 'white', 'audi', False)
auto_3 = WorkCar(70, 'grey', 'ford', False)
auto_4 = PoliceCar(150, 'white', 'ford', True)
auto_1.go()
auto_2.show_speed()
auto_3.stop()
auto_1.turn()
auto_4.police()
