#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to\
'http://0.0.0.0:5000/search_user' with the letter as a parameter.
"""

import sys
import requests


if __name__ == '__main__':
    letter = ""
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': letter})
    try:
        data = response.json()
        print("[{}] {}".format(data[id], data[name]))
    except JSONDecodeError:
        print("No result")
