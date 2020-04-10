#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me so the server reponds with "You got me!" in the body of the response.
curl -s 0.0.0.0:5000/catch_me -o /dev/null -w "You got me!"
