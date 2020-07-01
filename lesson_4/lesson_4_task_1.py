import sys

try:
    production_per_hour = int(sys.argv[1])
    rate_per_hour = int(sys.argv[2])
    prize = int(sys.argv[3])
    print(production_per_hour * rate_per_hour + prize)
except IndexError:
    print('Обязателен ввод трех параметров: выработка в часах, ставка в час, премия')
