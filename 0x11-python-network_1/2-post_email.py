#!/usr/bin/python3
"""
    Script takes in URL and email, sends POST request to
    passed URL with the email as a parameter, and displays
    body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as re:
            print(re.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
