array = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
out = [array[i] for i in range(0, len(array)) if array[:i].count(array[i]) == 0 and array[i + 1:].count(array[i]) == 0]
print(out)
