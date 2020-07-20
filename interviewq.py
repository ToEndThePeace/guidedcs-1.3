x = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
y = [
    "five",
    "twenty six",
    "nine hundred ninety nine",
    "twelve",
    "eighteen",
    "one hundred one",
    "fifty two",
    "forty one",
    "seventy seven",
    "six",
    "twelve",
    "four",
    "sixteen"
]

conversions = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
}


def parseToInt(string=""):
    # needs to return an int
    split_str = string.split(" ")
    int_val = 0
    is_hund = False
    for i, val in enumerate(split_str):
        x = len(split_str) - i - 1
        if split_str[x] != "hundred" and not is_hund:
            int_val += conversions[split_str[x]]
        elif is_hund:
            # read the hundreds place
            is_hund = False
            int_val += 100 * conversions[split_str[x]]
            pass
        else:
            # we hit a hundreds place, so we skip to the next iteration
            is_hund = True
    return int_val


def getDivBy3(arr):
    newArr = []
    for item in arr:
        if isinstance(item, int):
            if item % 3 == 0:
                newArr.append(item)
        elif isinstance(item, str):
            if parseToInt(item) % 3 == 0:
                newArr.append(item)
    return newArr


print(getDivBy3(x))
print(getDivBy3(y))


def pseudo(arr):
    """
    red every element in the array in a loop
    split the string into arr like
    for item in arr:
        splitstr = item.split(" ")
        converted = 0
        for i in range(len(splitstr)):
            if splitstr[i] != "hundred"
                x = len(item) - i - 1
                converted += mydict[arr[x]] <--- check a dictionary to
        else:
            converted += mydict[splitr[x - 1]]

    return result
    """
    pass
