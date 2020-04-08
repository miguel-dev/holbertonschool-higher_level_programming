#!/bin/bash
#Accepts a URL, sends a request to it and displays the size of the body of the response.
curl --head "$1" -s | grep -Po "Content-Length: \K(\d\d)"
