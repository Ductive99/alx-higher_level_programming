#!/usr/bin/env bash
# Takes in a URL - Displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2
