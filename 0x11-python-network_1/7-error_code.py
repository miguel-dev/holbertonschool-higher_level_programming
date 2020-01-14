#!/usr/bin/python3
"""Accepts a URL, sends a request to it and displays the body of response"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    sc = r.status_code
    try:
        r.raise_for_status()
        print(r.text)
    except:
        print("Error code: {}".format(r.status_code))
