#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_arr = len(my_list)
    for i in range(len_arr - 1, -1, -1):
        print("{:d}".format(my_list[i]))
