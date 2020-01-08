#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    division = 0
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except Exception:
            print("out of range")
        finally:
            new_list.append(division)
            division = 0

    return new_list
