class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Position('Иван', 'Петров', 'Продавец', 30000, 15000)
worker_1.get_full_name()
print(f'Должность: {worker_1.position}')
print(worker_1.get_total_income())
