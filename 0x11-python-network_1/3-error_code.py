#!/usr/bin/python3
"""Accepts a URL, sends a request to it and displays
the body of the response"""
import urllib.request
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code: " + str(e.code))
