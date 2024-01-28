#!/usr/bin/python3
"""
- Takes in a URL + Sends a request to it
- Displays the value of the X-Request-Id variable
"""
import urllib.request as request
import sys

url = sys.argv[1]

url_req = request.Request(url)

with request.urlopen(url_req) as response:
    print(response.headers.get('X-Request-Id'))
