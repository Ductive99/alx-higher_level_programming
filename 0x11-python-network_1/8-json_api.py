#!/usr/bin/python3
"""
Script that takes in a letter, and
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": letter}

    r = requests.post(url, data=data)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
