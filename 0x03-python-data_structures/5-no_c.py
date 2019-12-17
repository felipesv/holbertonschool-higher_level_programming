#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for i in range(0, len(my_string)):
        ascii_num = ord(my_string[i])
        if ascii_num != 67 and ascii_num != 99:
            new_str += my_string[i]
    return new_str
