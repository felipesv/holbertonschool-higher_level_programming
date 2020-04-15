#!/usr/bin/python3
# print 10 commits
import requests
import sys


if __name__ == '__main__':
    usr = sys.argv[2]
    rep = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(usr, rep)
    r = requests.get(url)
    try:
        json = r.json()
        for i in range(10):
            data = json[i]
            sha = data.get("sha")
            name = data.get("commit").get("author").get("name")
            print("{}: {}".format(sha, name))
    except Exception:
        pass
