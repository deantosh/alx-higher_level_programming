#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays\
the body of the response (decoded in utf-8)
"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            resp_body = response.read().decode('utf-8')
            print(resp_body)
    except HTTPError as e:
        err_msg = "Error code: {}".format(e.code)
        print(err_msg)
