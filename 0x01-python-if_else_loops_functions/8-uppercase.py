#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        uppLet = ord(str[i])
        print("{:c}".format(uppLet - 32 if uppLet > 95 else uppLet), end="")
    print("{:s}".format("\n"), end="")
