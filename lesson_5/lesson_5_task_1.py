with open('file_1.txt', 'w') as f:
    while True:
        user_input = input('Введите данные: ')
        if user_input == '':
            break
        else:
            print(user_input, file=f)
