class Worker:
    def __init__(self):
        self.name = 'Иван'
        self.surname = 'Иваныч'
        self.position = 'Директор'
        self._income = {'wage': 10000, 'bonus': 1000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.position} {self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker = Position()
print(worker.get_full_name())
print(worker.get_total_income())
