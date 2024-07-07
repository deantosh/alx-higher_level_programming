#!/usr/bin/python3
"""
Script fetches https://alx-intranet.hbtn.io/status.
Requirements:
  - You must use the package requests
  - You are not allow to import packages other than requests
"""
import requests


if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    res_type = "\t- type: {}".format(type(res.text))
    print(res_type)
    res_content = "\t- content: {}".format(res.text)
    print(res_content)
