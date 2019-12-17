#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val1 = 0
    val2 = 0
    if tuple_a:
        for i in range(0, 2 if len(tuple_a) > 2 else len(tuple_a)):
            if i % 2 == 0:
                val1 += tuple_a[i]
            else:
                val2 += tuple_a[i]
    if tuple_b:
        for i in range(0, 2 if len(tuple_b) > 2 else len(tuple_b)):
            if i % 2 == 0:
                val1 += tuple_b[i]
            else:
                val2 += tuple_b[i]

    res = (val1, val2)
    return res
