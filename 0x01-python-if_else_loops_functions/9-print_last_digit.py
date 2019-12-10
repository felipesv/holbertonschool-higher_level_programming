#!/usr/bin/python3
def print_last_digit(number):
    lastDig = abs(number) % 10
    print("{:d}".format(lastDig), end="")
    return lastDig
