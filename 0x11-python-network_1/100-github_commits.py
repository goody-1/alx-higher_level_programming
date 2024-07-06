#!/usr/bin/python3
"""
 Lists 10 commits from the most recent to oldest of the
    repository "rails" by the user "rails"
    Usage:
            ./100-github_commits.py <repo name> <owner>

- Use requests and sys packages
- The first argument will be the repository name
- The second argument will be the owner name
- Import no other package
- No need to check arguments passed to the script (number or type)
"""

import requests as req
from sys import argv
# from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = req.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(commits[i]["sha"]),
                  commits[i]['commit']['author']['name'])

    except Exception:
        pass
