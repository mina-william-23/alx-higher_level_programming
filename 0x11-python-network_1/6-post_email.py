#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
USAGE: ./2-post_email.py <URL> <email>"""


# curl -s -L -X POST -d email=sys.argv[2] sys.argv[1]
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    request = requests.post(url, data)
    print(request.text)
