#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.

- Use requests and sys packages
- The letter must be sent in the variable q
- Import no other package
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty,
 display the id and name like this: [<id>] <name>
- Otherwise:
    - Display Not a valid JSON if the JSON is invalid
    - Display No result if the JSON is empty
"""

import requests as req
from sys import argv

if __name__ == "__main__":
    if len(argv[1]) > 1:
        letter = argv[1]
    else:
        letter = ""

    payload = {"q": letter}

    url = "http://0.0.0.0:5000/search_user"
    r = req.post(url, data=payload)

    try:
        r.raise_for_status()
        response = r.json()
        if len(response) > 0:
            print("[{:d}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
