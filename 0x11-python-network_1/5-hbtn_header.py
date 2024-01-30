#!/usr/bin/python3
"""
- Takes in a URL, Sends a request to it
- Displays the value of the `X-Request-Id` variable
"""
if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
