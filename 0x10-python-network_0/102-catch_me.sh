#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me where it responds with You got me! with the body of the response.
curl -sLX PUT -d user_id=98 -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
