#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays\
the body of the response.
"""

import sys
import requests


if __name__ == '__main__':
    try:
        url = sys.argv[1]
        response = requests.get(url)
        # raise a HTTPError for unsuccessful status code.
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e}")
