#!/usr/bin/python3
"""Accepts a URL, sends a request to it and displays the value of the X-Request-Id"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
