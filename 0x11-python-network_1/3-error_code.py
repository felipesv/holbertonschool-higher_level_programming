#!/usr/bin/python3
# Error code
import urllib.request
import sys


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as reponse:
            print(reponse.read().decode("utf-8"))
    except urllib.error.URLError as error:
        print("Error code: {}".format(error.__dict__["code"]))
