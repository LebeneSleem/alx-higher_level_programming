#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def fetch_hbtn_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io and displays the response.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        content_type = response.info().get_content_type()
        content_encoding = response.info().get_content_charset()

        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        if content_encoding:
            decoded_content = body.decode(content_encoding)
            print(f"    - utf8 content: {decoded_content}")
        else:
            print(f"    - utf8 content: Unable to decode")

if __name__ == "__main__":
    fetch_hbtn_status()
