def common_letters(first, second):
    common = []
    for i in set(first):
        for j in set(second):
            if i == j:
                common.append(i)
    return common


common_letters("house", "computers")

