#!/bin/bash
#  displays the size of the body - curl -sI "$1" | grep Content-Length | cut -d' ' -f2
status_code=$(curl -sL -w "%{http_code}" -o /dev/null "$1")
if [ "$status_code" -eq 200 ]; then
    curl -sL "$1"
fi
