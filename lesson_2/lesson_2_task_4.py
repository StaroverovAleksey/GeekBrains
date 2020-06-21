user_input = input('Введите слова через пробел: ').split(' ')
for i in range(0, len(user_input)):
    print(i + 1, user_input[i][0:10])
