user_input = input('Введите список элементов через пробел: ')
user_list = user_input.split(' ')
output_list = []
for item in range(0, len(user_list), 2):
    print(item)
    try:
        output_list.append(user_list[item + 1])
        output_list.append(user_list[item])
    except IndexError:
        output_list.append(user_list[item])
print(output_list)
