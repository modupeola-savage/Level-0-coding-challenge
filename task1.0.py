def common_letters(first, second):
    common = "Common letters: "
    for i in set(first):
        for j in set(second):
            if i == j:
                common += i + ","
    return common


common_letters("house", "computers")
