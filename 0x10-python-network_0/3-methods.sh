#!/bin/bash
# Accepts a URL and displays all available HTTP methods.
curl -siX OPTIONS "$1" | grep -Po "(?<=Allow: )(.*)$"
