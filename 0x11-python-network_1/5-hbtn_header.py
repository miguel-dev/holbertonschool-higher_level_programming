#!/usr/bin/python3
"""Get a URL, send a request to it and display the value of the variable
X-Request-Id in the response header"""


if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    dict_headers = r.headers
    print(dict_headers.get("X-Request-Id"))
