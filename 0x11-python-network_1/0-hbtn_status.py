#!/usr/bin/python3

from urllib.request import Request, urlopen

req = Request("https://alx-intranet.hbtn.io/status")
with urlopen(req) as response:
    the_page = response.read()
    print("Body response:")
    page_type = "\t- type: {}".format(type(the_page))
    print(page_type)
    page_content = "\t- content: {}".format(the_page)
    print(page_content)
    utf_content = "\t- utf8 content: {}".format(the_page.decode('utf-8'))
    print(utf_content)
