#!/bin/bash
# Sends a request to an URL passed as an argument, and displays only the status code of the response.
curl -LIs "$1" -o /dev/null -w "%{http_code}"
