def convert_time(x):
    p = x // 60
    y = x % 60

    if p <= 1:
        print(str(p) + "hour")
    else:
        print(str(p) + "hours")
    if y <= 1:
        print(str(y) + "miniute")
    else:
        print(str(y) + "minutes")


convert_time(71)

