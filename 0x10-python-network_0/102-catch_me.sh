#!/bin/bash
# Sends a request to a URL, displays only the status code of the response.
curl -s -o /dev/null -w 'You got me!' "http://0.0.0.0:5000/catch_me"
