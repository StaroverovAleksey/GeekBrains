class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, weight, depth):
        return self._length * self._width * weight * depth


road = Road(20, 5000)
print(road.calculate(25, 5))
