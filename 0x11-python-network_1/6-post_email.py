#!/usr/bin/python3
# sends a POST request
import requests
import sys


if __name__ == '__main__':
    values = [("email", sys.argv[2])]
    r = requests.post(sys.argv[1], data=values)
    print(r.__dict__["_content"].decode("utf-8"))
