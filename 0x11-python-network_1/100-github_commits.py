#!/usr/bin/python3
"""Lists 10 commits of a given repository and user"""


if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    list_res = r.json()
    for i in range(10):
        print("{}: {}".format(list_res[i].get("sha"),
                              list_res[i].get("author").get("name")))
