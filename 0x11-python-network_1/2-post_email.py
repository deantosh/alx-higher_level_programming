#!/usr/bin/python3
"""
Script takes in a URL and an email, sends a POST request to the passed\
URL with the email as a parameter, and displays the body of the\
response (decoded in utf-8).
"""

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == '__main__':
    # get args
    url, email = sys.argv[1:]

    # create data as dict object
    value = {}
    value["email"] = email

    data = urlencode(value).encode('ascii')  # data to bytes
    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
