#!/usr/bin/python3
"""
Script that takes in a URL sends a request to the URL and
 displays the body of the response.

- Use requests and sys packages
- If the HTTP status code is greater than or equal to 400, print: Error code:
 followed by the value of the HTTP status code
- Import no other package
- No need to check arguments passed to the script (number or type)
"""

import requests as req
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    r = req.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
