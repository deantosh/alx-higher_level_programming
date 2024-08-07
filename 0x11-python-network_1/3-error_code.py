#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and dipllays the body
of the response (decoded in utf-8).
Requirements:
  - You have to manage urllib.error.HTTPError exceptions and print:
      Error code: followed by the HTTP status code
  - You are not allowed to import other packages than urllib and sys
  - You must use the with statement
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
