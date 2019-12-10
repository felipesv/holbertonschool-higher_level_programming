#!/usr/bin/python3
def islower(c):
        asciiValue = ord(c)
        if asciiValue >= 65 and asciiValue <= 90:
                return False
        return True
