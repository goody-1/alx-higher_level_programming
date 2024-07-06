#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
 of the X-Request-Id variable found in the header of the response.

- Use requests and sys packages
- The value of this variable is different for each request
- No need to check script arguments (number and type)
"""

import requests as req
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = req.get(url)

    print(r.headers.get('X-Request-Id'))
