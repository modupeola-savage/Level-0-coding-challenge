def convert_time(x):
    hr = x // 60
    min = x % 60

    if hr > 1 and min > 1:
        print(str(hr) + " " + "hours" + "," + " " + str(min) + " " + "minutes")
    elif hr <= 1 and min <= 1:
        print(str(hr) + " " + "hour" + "," + " " + str(min) + " " + "minute")
    if hr > 1 and min <= 1:
        print(str(hr) + " " + "hours" + "," + " " + str(min) + " " + "minute")
    elif hr <= 1 and min > 1:
        print(str(hr) + " " + "hour" + "," + " " + str(min) + " " + "minutes")


convert_time(133)

