#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status

- Use requests package
- Import no other package
"""

import requests as req

if __name__ == "__main__":
    r = req.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
