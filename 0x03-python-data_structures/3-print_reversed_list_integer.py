#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_arr = len(my_list)
    my_list.reverse()
    for i in range(0, len_arr):
        print("{:d}".format(my_list[i]))
