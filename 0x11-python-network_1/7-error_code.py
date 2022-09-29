#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    q = requests.get(url)
    try:
        q.raise_for_status()
        print(q.text)
    except Exception as e:
        print("Error code: {}".format(q.status_code))
