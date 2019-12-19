#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list1 = set(set_1)
    new_list2 = set(set_2)
    return new_list1 ^ new_list2
