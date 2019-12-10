#!/usr/bin/python3
def islower(c):
        asciiValue = ord(c)
        if asciiValue >= 65 and asciiValue <= 90:
                return False
        elif asciiValue >= 48 and asciiValue <= 57:
                return False
        return True
