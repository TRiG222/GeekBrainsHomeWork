class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки c помощью "{self.title}"')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки с помощью "{self.title}"')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки с помощью "{self.title}"')


Pen = Pen('Ручка')
Pen.draw()
Pencil = Pencil('Карандаш')
Pencil.draw()
Handle = Handle('Маркер')
Handle.draw()
