#!/bin/bash
#Script that takes a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -oP "(?<=^Allow:\s)(\w.*)$"
