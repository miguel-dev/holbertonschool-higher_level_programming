#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print("Body response:")
        print("    - type: {}".format(type(r)))
        print("    - content: {}".format(r))
        print("    - utf8 content: {}".format(r.decode('utf-8')))
