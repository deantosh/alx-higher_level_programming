#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays the body
of the response.
Requirements:
  - If the HTTP status code is greater than or equal to 400, print:
    Error code: followed by the value of the HTTP status code
  - You must use the packages requests and sys
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
