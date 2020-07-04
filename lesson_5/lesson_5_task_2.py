with open('file_1.txt') as f:
    file_array = f.readlines()
print(f'В файле {len(file_array)} строк(и)')
for i in enumerate(file_array):
    print(f'В строке №{i[0]}: {len(i[1].split())} слов(а)')
