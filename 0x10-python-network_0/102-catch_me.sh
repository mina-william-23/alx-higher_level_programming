#!/bin/bash
# Sends a request to a URL, displays only the status code of the response.
curl -sL -X POST -d "bla=bla" "0.0.0.0:5000/catch_me"
