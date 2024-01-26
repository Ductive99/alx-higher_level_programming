#!/usr/bin/env bash
# Sends a DELETE request to the URL passed as 1st arg and the displays the body of the response
curl -sX DELETE "$1"
