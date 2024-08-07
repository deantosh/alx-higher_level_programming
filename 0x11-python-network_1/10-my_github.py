#!/usr/bin/python3
"""
Script takes your GitHub credentials (username and password)\
and uses the GitHub API to display your id.
"""

import sys
import requests


if __name__ == '__main__':
    username, password = sys.argv[1:]

    # GITHUB api users method
    github_url = "https://api.github.com/user"

    credentials = (username, password)

    # pass authorization header to authenticate user
    res = requests.get(github_url, auth=credentials)

    # convert to JSON
    user_data = res.json()

    # get user id
    user_id = user_data.get('id')

    print(user_id)
