#!/bin/bash
# curl -sI "$1" | grep Content-Length | cut -d' ' -f2
curl -s -o /dev/null -w "%{size_download}\n" "$1"
