#!/usr/bin/python3
"""Accepts a URL, sends a request to it and displays the body of the response
decoded in utf-8"""

if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            print(res.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(e.code)
