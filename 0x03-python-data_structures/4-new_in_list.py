#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_arr = len(my_list)
    copy = []
    for i in range(0, len_arr):
        copy.append(my_list[i])

    if (idx < 0) or ((idx + 1) > len_arr):
        return copy

    copy[idx] = element
    return copy
