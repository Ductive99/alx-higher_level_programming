#!/usr/bin/python3
"""
- Takes in a URL and sends a request to it
- Display the body of the response
- Using the request module
"""
if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
