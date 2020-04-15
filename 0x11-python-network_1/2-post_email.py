#!/usr/bin/python3
"""Accepts a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the
responsei encoded in utf-8"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    email = {'email' : sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))
