#!/usr/bin/python3
# sends a POST request
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    data = {}
    data["email"] = sys.argv[2]
    url_values = urllib.parse.urlencode(data).encode("utf-8")
    full_url = urllib.request.Request(sys.argv[1], url_values)
    with urllib.request.urlopen(full_url) as reponse:
        print(reponse.read().decode("utf-8"))
