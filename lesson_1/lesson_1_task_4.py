user_number = input('Введите число: ')
max_number = user_number[0]
count = 1
while count < len(user_number):
    if int(max_number) < int(user_number[count]):
        max_number = user_number[count]
    count += 1
print(max_number)
