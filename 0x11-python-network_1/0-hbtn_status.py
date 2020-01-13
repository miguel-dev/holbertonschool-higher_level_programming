#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    status = response.read()
    print("Body response:")
    print("\t- type: " + str(type(status)))
    print("\t- content: " + str(status))
    print("\t- utf8 content: " + str(status.decode("utf8")))
