#!/usr/bin/python3
"""
    list 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commit = req.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                commit[x].get("sha"),
                commit[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
