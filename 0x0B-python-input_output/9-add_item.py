#!/usr/bin/python3

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

l = []

try:
    l = list(load_from_json_file("add_item.json"))
except FileNotFoundError:
    save_to_json_file(l, "add_item.json")

l.extend(sys.argv[1:])
save_to_json_file(l, "add_item.json")
