#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        valuesInt = my_list[i]
        try:
            print("{:d}".format(valuesInt), end="")
            cnt += 1
        except Exception:
            pass
    print("")
    return cnt
