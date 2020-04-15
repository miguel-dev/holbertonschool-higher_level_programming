#!/usr/bin/python3
"""Accepts URL, sends a request to the URL and displays the value
of the X-Request-Id variable in the header of the response"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        r = response.headers
        dict_headers = dict(r)
        print(dict_headers.get("X-Request-Id"))
