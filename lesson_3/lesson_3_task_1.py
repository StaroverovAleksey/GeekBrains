user_number_1 = int(input('Введите первое число: '))
user_number_2 = int(input('Введите второе число: '))


def divide_numbers(dividend, divider):
    try:
        return round(dividend / divider, 2)
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


print(divide_numbers(user_number_1, user_number_2))
