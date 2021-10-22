def temp_celsius(x):
    farenheit = (9 / 5 * x) + 32
    to_farenheit = str(farenheit) + "F"
    return to_farenheit


temp_celsius(20)


def temp_farenheit(y):
    celsius = 5 / 9 * (y - 32)
    to_celsius = str(celsius) + "C"
    return to_celsius


temp_farenheit(98.6)
