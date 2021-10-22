def returnVowels(string):
    vowels = "aeiou"
    result = set()
    for x in string.lower():
        if x in vowels:
            result.add(x)
    print("returnVowels:", result)


returnVowels("Umuzi")

