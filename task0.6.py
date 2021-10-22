def maximum_number(x, y, z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)


maximum_number(10, 12, 14)
