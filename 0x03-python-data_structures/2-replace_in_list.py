#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx >= 0):
        len_arr = len(my_list)
        if ((idx + 1) <= len_arr):
            my_list[idx] = element
    return my_list
