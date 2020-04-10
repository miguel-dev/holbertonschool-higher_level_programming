#!/bin/bash
# Accepts a URL, sends a GET request to it and displays body of response.
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
