#!/bin/bash
#Script that sends a request to a URL passed as an argument and distrplays only the status code of the response.
curl -LIs "$1" -o /dev/null -w '%{http_code}'
