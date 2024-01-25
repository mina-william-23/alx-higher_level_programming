#!/bin/bash
# status_code=$(curl -sL -w "%{http_code}" -o /dev/null "$1")--- if [ "$status_code" -eq 200 ]; then curl -sL "$1" fi
curl -sL "$1"
