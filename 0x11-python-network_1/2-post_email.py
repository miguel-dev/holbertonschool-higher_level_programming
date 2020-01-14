#!/usr/bin/python3
"""Accept an URL and email, send a POST request to the passed URL with the email
as a parameter and displays the body of the response (decoded in utf-8)"""
import urllib.request
import sys
if __name__ == "__main__":
    values = {"email" : sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
