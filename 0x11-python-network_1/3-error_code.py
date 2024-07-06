#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
 of the response (decoded in utf-8).

- Use urllib and sys packages
- Manage urllib.error.HTTPError exceptions and print: Error code: followed by
 the HTTP status code
- Import no other package
- Use with statement
- No need to check arguments passed to the script (number or type)
"""

from urllib import (request as req,
                    error)
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    r = req.Request(url)
    try:
        with req.urlopen(r) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
