#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    from calculator_1 import add, sub, mul, div

    lenAr = len(sys.argv)
    if (lenAr != 4):
        print("{:s}".
              format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    opr = sys.argv[2]
    if (opr != "+" and opr != "-" and opr != "*" and opr != "/"):
        print("{:s}".
              format("Unknown operator. Available operators: +, -, * and /"))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (opr == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if (opr == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if (opr == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if (opr == "/"):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
