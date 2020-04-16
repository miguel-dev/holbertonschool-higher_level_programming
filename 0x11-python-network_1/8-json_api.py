#!/usr/bin/python3
"""Get a letter and send a POST request to
http://0.0.0.0:5000/search_user with the
letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    letter = ""
    if len(sys.argv) >= 2:
        letter = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        j = r.json()
        if j == {}:
            print("No result")
        else:
            print("[{:d}] {:s}".format(j.get("id"), j.get("name")))
    except:
        print("Not a valid JSON")
