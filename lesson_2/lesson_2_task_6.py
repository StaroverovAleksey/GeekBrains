products_list = []
user_trigger = 1
while user_trigger:
    user_name = input('Введите название товара: ')
    user_price = int(input('Введите цену товара: '))
    user_count = int(input('Введите кличество товара: '))
    user_unit = input('Введите единицу измерения товара: ')
    products_list.append((user_trigger, {'название': user_name,
                                         'цена': user_price,
                                         'количество': user_count,
                                         'ед': user_unit}
                          ))
    user_request = input('Внести новый товар? (y / n): ')
    user_trigger = user_trigger + 1 if user_request == 'y' else False
output_dict = {'название': [],
               'цена': [],
               'количество': [],
               'ед': []}
for i in products_list:
    output_dict['название'].append(i[1]['название'])
    output_dict['цена'].append(i[1]['цена'])
    output_dict['количество'].append(i[1]['количество'])
    output_dict['ед'].append(i[1]['ед'])
print(output_dict)
