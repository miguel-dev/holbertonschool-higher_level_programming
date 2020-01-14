#!/usr/bin/python3
"""Accepts in a URL, sends a request to it and displays the value
of the variable X_Request-Id in the response header"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
