#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id

- Use requests and sys packages
- Use Basic Authentication with a personal access token as password to
access to your information (only read:user permission is needed)
- Import no other package
- The first argument will be your username
- The second argument will be your password (in your case, a
personal access token as password)
- No need to check arguments passed to the script (number or type)
"""

import requests as req
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])

    r = req.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
