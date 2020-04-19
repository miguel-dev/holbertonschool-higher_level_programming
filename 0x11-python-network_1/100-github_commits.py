#!/usr/bin/python3
"""Lists 10 commits of a given repository and user"""


if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    list_res = r.json()
    r = 10

    if len(list_res) < 10:
        r = len(list_res)

    for i in range(r):
        dict_commit = list_res[i].get("commit")
        if (dict_commit):
            dict_author = dict_commit.get("author")
        if (dict_author):
            dict_name = dict_author.get("name")
        print("{}: {}".format(list_res[i].get("sha"), dict_name))
