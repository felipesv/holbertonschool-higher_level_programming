#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    lenAr = (len(sys.argv) - 1) if len(sys.argv) != 1 else 0
    print("{:d} {:s}{:s}"
          .format(lenAr, "argument" if lenAr == 1 else "arguments",
                  "." if lenAr == 0 else ":"))
    for i in range(0, lenAr):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
