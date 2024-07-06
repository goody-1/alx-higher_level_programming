#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
 URL with the email as a parameter, and displays the body of the response
  (decoded in utf-8)

- Use urllib and sys packages
- The email must be sent in the email variable
- Import no other package
- Use with statement
- No need to check arguments passed to the script (number or type)
"""

from urllib import (request as req,
                    parse)
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')

    r = req.Request(url, data)

    with req.urlopen(r) as response:
        page = response.read()

        print(page.decode('utf-8'))
