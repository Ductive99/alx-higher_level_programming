#!/usr/bin/python3
"""
- Takes in a URL and an email
- Sends a POST request to it
- Displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
