def my_func(x, y, z):
    if x <= y and x <= z:
        return y + z
    elif y <= x and y <= z:
        return x + z
    return x + y


print(my_func(1, 2, 3))
