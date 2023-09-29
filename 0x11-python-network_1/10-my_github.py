#!/usr/bin/python3
"""
    script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", authen=authen)
    print(req.json().get("id"))
