#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed
 URL with the email as a parameter, and displays the body of the response
  (decoded in utf-8)

- Use requests and sys packages
- The email must be sent in the email variable
- Import no other package
- No need to check arguments passed to the script (number or type)
"""

import requests as req
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}

    r = req.post(url, data=payload)
    print(r.text)
