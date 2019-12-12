#!/usr/bin/python3
import hidden_4
if (__name__ == "__main__"):
    arg = dir(hidden_4)
    for i in range(0, len(arg)):
        if arg[i].find("__") == -1:
            print(arg[i])
