#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status

- Use urllib
- Import no other package
- Use with statement
"""

import urllib.request as u

if __name__ == "__main__":
    with u.urlopen('https://alx-intranet.hbtn.io/status') as response:
        page = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
