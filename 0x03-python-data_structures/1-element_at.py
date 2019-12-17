#!/usr/bin/python3
def element_at(my_list, idx):
    len_arr = len(my_list)
    if (idx < 0) or ((idx + 1) > len_arr):
        return None
    return (my_list[idx])
