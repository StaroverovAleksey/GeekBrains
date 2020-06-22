user_input = input('Вводите слова через пробел: ').split()
output = ' '.join(map(lambda word: word.capitalize(), user_input))
print(output)

#Не вижу смысла использовать для столь атомарной операции именованную функцию. И решение в одну строчку красивее.