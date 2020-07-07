class Stationery:
    def __init__(self, title):
        self.title = title

    def darw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def darw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def darw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def darw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen('ручка')
pen.darw()
pen = Pencil('карандаш')
pen.darw()
pen = Handle('маркер')
pen.darw()
