#!/usr/bin/python3
"""
Script that list 10 commits of 'rails' repository by user 'rails'.
"""

import sys
import requests


if __name__ == '__main__':
    repo, owner = sys.argv[1:]

    github_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(github_url)

    commits = res.json()

    try:
        for i in range(10):
            id = commits[i].get('sha')
            name = commits[i].get('commit').get('author').get('name')
            res_str = "{}: {}".format(id, name)
            print(res_str)

    except IndexError:
        pass  # do nothing
