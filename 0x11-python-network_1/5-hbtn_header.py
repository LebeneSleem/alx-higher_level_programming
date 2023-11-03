#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the value
"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
x_request_id = response.headers.get('X-Request-Id')

if x_request_id:
    print(x_request_id)
