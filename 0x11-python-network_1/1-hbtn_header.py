#!/usr/bin/python3
"""Accepts a URL, sends a request to it and shows the value of X-Request-Id"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
