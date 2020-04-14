#!/usr/bin/python3
# sends a request to the URL
import requests


if __name__ == '__main__':
    r = requests.get("https://intranet.hbtn.io/status")
    print(r.__dict__["headers"]["X-Request-Id"])
