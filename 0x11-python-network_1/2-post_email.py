#!/usr/bin/python3
"""
Script takes in a URL and an email, sends a POST request to the passed
URL with thee email as a parameter, and displays the body of the
response (decoded in utf-8).
Requirements:
  - The email must be sent in the email variable
  - You are not allowed to import packages other than urllib and sys
  - You must use the with statement
"""
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == '__main__':
    # get args
    url, email = sys.argv[1:]
    # create data as dict object
    new_dict = {}
    new_dict["email"] = email

    data = urlencode(new_dict).encode('ascii')  # data to bytes
    req = Request(url, data=data, method='POST')
    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
