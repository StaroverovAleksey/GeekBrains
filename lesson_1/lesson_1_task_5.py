proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if costs > proceeds:
    print(f'Убыток составил {costs - proceeds}')
elif costs == proceeds:
    print(f'Прибыли нет')
elif costs < proceeds:
    print(f'Рентабельность составила {round((proceeds / costs), 2)}')
    cost_users = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы на одного сотрудникка составила {round(((proceeds - costs) / cost_users), 2)}')
