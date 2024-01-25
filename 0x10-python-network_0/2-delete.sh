#!/bin/bash
# I for header
curl -sI "$1" | grep Allow | cut -d' ' -f2-
