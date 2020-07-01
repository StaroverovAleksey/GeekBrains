from itertools import cycle

array = [1, 5, 8, 4]
counter = 0
stop = int(input('Введите количество циклов: '))
for i in cycle(array):
    print(i)
    counter += 1
    if counter / len(array) >= stop:
        break
