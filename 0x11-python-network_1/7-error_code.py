#!/usr/bin/python3
"""Accepts a URL, sends a request to it and displays the body of response"""
import requests
import sys
r = requests.get(sys.argv[1])
sc = r.status_code
if (sc >= 400):
    print("Error code: {}".format(sc))
else:
    print(r.text)
