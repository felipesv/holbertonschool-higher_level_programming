#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i in a_dictionary.items():
            if i[1] == max(a_dictionary.values()):
                return i[0]
    return None
