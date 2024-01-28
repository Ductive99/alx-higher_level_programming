#!/usr/bin/python3
"""
- Takes in a URL + Sends a request to it
- Displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import urllib.request as request
    import sys

    url_req = request.Request(sys.argv[1])

    with request.urlopen(url_req) as response:
        print(response.headers.get('X-Request-Id'))
