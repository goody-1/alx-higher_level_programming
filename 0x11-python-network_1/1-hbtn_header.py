#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
 of the X-Request-Id variable found in the header of the response.

- Use urllib and sys packages
- Import no other package
- Use with statement
"""

import urllib.request as u
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with u.urlopen(url) as response:
        page = response.read()

        print(dict(response.headers).get('X-Request-Id'))
