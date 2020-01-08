#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format())
    except IndexError:
        return False
    return True
