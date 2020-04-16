#!/usr/bin/python3
"""Get a URL, sends a request to it and displays the body
of the response. Handles error codes."""


if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    elif r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
