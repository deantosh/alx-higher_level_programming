#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.
Requirements:
  - You must use the packages requests and sys
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get('X-Request-Id')
    print(value)
