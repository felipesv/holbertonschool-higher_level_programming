#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for i in range(x):
        valuesInt = my_list[i]
        try:
            print("{:d}".format(valuesInt), end="")
        except Exception:
            pass
    print("")
    return i
