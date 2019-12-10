#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
print("Last digit of {:d} is {:d} and is".format(number, lastDigit), end="")
if lastDigit > 5:
    print("{:s}".format(" greater than 5"))
elif lastDigit == 0:
    print("{:s}".format(" 0"))
elif lastDigit < 6:
    print("{:s}".format(" less than 6 and not 0"))
