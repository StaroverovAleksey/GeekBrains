import time


class TrafficLight:
    def __init__(self):
        self.color = ''
        self._running()

    def _running(self):
        while True:
            self.color = 'red'
            print(self.color)
            time.sleep(7)
            self.color = 'yellow'
            print(self.color)
            time.sleep(2)
            self.color = 'green'
            print(self.color)
            time.sleep(5)


light = TrafficLight()
