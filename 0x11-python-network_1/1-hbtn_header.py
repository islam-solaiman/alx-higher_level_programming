#!/usr/bin/python3
"""
    Script that takes URL, sends a request to URL and displays
    value of the X-Request-Id variable found in header of response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
