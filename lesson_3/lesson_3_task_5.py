def counter():
    amount = 0
    while True:
        user_input = input('Введите числа ("q" для завершения): ').split()
        for i in user_input:
            if i.upper() == 'Q':
                print(amount)
                return
            else:
                amount = amount + int(i)
        print(amount)


counter()
