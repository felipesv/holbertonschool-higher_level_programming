#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
        res = 0
        for i in range(0, len(sys.argv) - 1):
                res += int(sys.argv[i + 1])
        print("{:d}".format(res))
