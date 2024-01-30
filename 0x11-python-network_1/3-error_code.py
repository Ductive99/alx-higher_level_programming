#!/usr/bin/python3
"""
- Takes in a URL
- Sends a request to it
- Displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    import sys

    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
