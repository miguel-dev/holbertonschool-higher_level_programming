#!/bin/bash
#Script that sends a request to a URL passed as an argument and distrplays only the status code of the response.
curl -Is "$1" | grep -Po "\b(\d{3})\b" | tr '\n' '\0'
