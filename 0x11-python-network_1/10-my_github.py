#!/usr/bin/python3
"""
Script takes your GitHub credentials (username and password)\
and uses the GitHub API to display your id.
"""

import sys
import requests


if __name__ == '__main__':
    username, password = sys.argv[1:]
    github_url = f"https://api.github.com/users/{username}"
    token = {'Authorization': password}

    # pass authorization header to authenticate user
    res = requests.get(github_url, headers=token)

    # convert to json
    user_data = res.json()

    # get user id
    id = user_data.get('id')

    # display id
    print(id)
