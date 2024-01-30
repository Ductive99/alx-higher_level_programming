#!/usr/bin/python3
"""
Takes GitHub credentials (username and password)
and uses the GitHub API to display user's id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(sys.argv[1], argv[2]))
    print(response.json().get("id"))
