from itertools import count

start = int(input('Введите начальное число: '))
stop = int(input('Введите конечное число: '))
for i in count(start):
    print(i)
    if i == stop:
        break
