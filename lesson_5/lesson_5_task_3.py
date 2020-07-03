with open('file_3.txt') as f:
    file_array = f.readlines()
low_salary = []
count = 0
for i in file_array:
    count += int(i.split()[1])
    if int(i.split()[1]) < 20000:
        low_salary.append(i.split()[0])
print(f'Сотрудники, имеющие ЗП менее 20 000: {", ".join(low_salary)}')
print(f'Средняя ЗП: {int(count / len(file_array))}')
