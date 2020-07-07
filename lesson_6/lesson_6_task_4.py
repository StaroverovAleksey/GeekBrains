class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'white'
        self.name = 'car'
        self.is_police = False

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'turn to {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed) if self.speed <= 60 else print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed) if self.speed <= 40 else print('Превышение скорости!')


class PoliceCar(Car):
    pass


townCar = TownCar()
townCar.speed = 61
townCar.show_speed()
