#!/usr/bin/python3
"""Function that find a peak"""

def find_peak(list_of_integers):
    """Function that find a peak"""
    if type(list_of_integers) == list:
        len_list = len(list_of_integers)
        if len_list == 0:
            return None
        elif len_list == 1:
            return list_of_integers[0]
        elif len_list == 2:
            return max(list_of_integers)
        else:
            prev_number = list_of_integers[int(len_list / 2) - 1]
            middle_number = list_of_integers[int(len_list / 2)]
            next_number = list_of_integers[int(len_list / 2) + 1]
            
            if middle_number > prev_number and middle_number > next_number:
                return middle_number
            elif middle_number < prev_number:
                newList = list_of_integers[int(len_list / 2) - 1:]
                return find_peak(newList)
            else:
                newList = list_of_integers[int(len_list / 2) + 1:]
                return find_peak(newList)

    return None
