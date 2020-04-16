#!/usr/bin/python3
"""Takes Github credentials (username and password)
and uses the Github API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    dict_response = r.json()
    print(dict_response.get('id'))
