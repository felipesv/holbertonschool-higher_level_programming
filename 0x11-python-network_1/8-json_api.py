#!/usr/bin/python3
# JSON reponse
import requests
import sys


if __name__ == '__main__':
    try:
        data = [("q", sys.argv[1])]
    except Exception:
        data = [("q", "")]
    r = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        if len(r.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
    except ValueError:
        print("Not a valid JSON")
