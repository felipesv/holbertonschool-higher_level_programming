#!/usr/bin/python3
# sends a request to the URL
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    try:
        print(r.__dict__["headers"]["X-Request-Id"])
    except Exception:
        print("None")
