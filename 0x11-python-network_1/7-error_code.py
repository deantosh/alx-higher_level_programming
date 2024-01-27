#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays\
the body of the response.
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    code = response.status_code
    if code >= 400:
        err_msg = "Error code: {}".format(code)
        print(err_msg)
