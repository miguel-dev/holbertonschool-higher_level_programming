#!/bin/bash
# Sends a JSON POST request to an URL passed as an argument, and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
