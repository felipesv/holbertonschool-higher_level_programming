#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if type(roman_string) is not str:
        return 0

    lenS = len(roman_string)
    res = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(lenS):
        posNxt = i + 1

        if posNxt < lenS and dic[roman_string[posNxt]] > dic[roman_string[i]]:
            res = res - dic[roman_string[i]]
        else:
            res = res + dic[roman_string[i]]

    return res
