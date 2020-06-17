user_sec = int(input('Введите количество секунд: '))
hours = user_sec // 3600
minutes = (user_sec % 3600) // 60
sec = ((user_sec % 3600) % 60) % 60
print(f'{hours:02}:{minutes:02}:{sec:02}')
