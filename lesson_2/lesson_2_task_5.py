user_input = int(input('Введите число: '))
my_list = [7, 5, 3, 3, 2]
for i in range(0, len(my_list)):
    if my_list[i] < user_input:
        my_list.insert(i, user_input)
        break
print(my_list)
