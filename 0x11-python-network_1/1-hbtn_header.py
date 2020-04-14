#!/usr/bin/python3
# sends a request to the URL
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as reponse:
        header = reponse.info().__dict__["_headers"]
        header = [item[1] for item in header if item[0] == "X-Request-Id"]
        print(header[0])
