start = int(input('Введите результат первого дня: '))
finish = int(input('Введите финальный результат: '))
day = 1
while start < finish:
    start = round(start * 1.1, 2)
    day += 1
print(day)
