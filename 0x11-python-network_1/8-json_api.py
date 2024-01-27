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
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))

    except JSONDecodeError:
        print("Not a valid JSON")
