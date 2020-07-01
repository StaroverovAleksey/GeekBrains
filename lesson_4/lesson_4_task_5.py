from functools import reduce

out = reduce(lambda i, j: i + j, [i for i in range(100, 1001) if i % 2 == 0])
print(out)
