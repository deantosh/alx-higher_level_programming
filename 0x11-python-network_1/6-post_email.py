#!/usr/bin/python3
"""
Script takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays
the body of the response.
Requirements:
  - The email must be sent in the variable email
  - You must use the packages requests and sys
  - You are not allowed to import packages other than requests and sys
"""
import sys
import requests


if __name__ == '__main__':
    url, email = sys.argv[1:]
    response = requests.post(url, data={'email': email})
    print(response.text)
