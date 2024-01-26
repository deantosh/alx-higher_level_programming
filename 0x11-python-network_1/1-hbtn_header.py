#!/usr/bin/python3

import sys
from urllib.request import Request, urlopen

# get url passed as argument
url = sys.argv[1]

req = Request(url)

with urlopen(req) as response:
    # get headers
    headers = response.headers
    value = headers.get('X-Request-Id')
    print(value)
