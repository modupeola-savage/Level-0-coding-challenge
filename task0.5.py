def area_of_tiangle(a, b, c):
    s = 1 / 2 * (a + b + c)
    x = (s - a) * (s - b) * (s - c)
    y = s * x
    z = y ** (1 / 2)
    print(z)


area_of_tiangle(3, 4, 5)
