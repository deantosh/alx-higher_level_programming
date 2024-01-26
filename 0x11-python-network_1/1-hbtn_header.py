#!/usr/bin/python3
"""Script takes in a URL, sends a request to the URL and displays\
the value of the X-Request-Id variable found in the header of the\
response.
"""
import sys
from urllib.request import Request, urlopen


if __name__ == '__main__':
    # get url passed as argument
    url = sys.argv[1]

    req = Request(url)

    with urlopen(req) as response:
        # get headers
        headers = response.headers
        value = headers.get('X-Request-Id')
        print(value)
