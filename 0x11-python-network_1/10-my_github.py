#!/usr/bin/python3
# git auth
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(r.json()["id"])
    except Exception:
        print("None")
