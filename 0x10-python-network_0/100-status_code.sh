#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -s -o localhost/catch_me -w "You got me!" -L
