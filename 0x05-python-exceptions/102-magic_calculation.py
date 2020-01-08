#!/usr/bin/python3
def magic_calculation(a, b):
    val = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            val += (a ** b) / i
        except Exception:
            val = b + a
            break
    return val
