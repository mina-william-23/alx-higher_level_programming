#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).

manage urllib.error.HTTPError exceptions
print: Error code: followed by the HTTP status code
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print('Error code: {}'.format(request.status_code))
    else:
        print(request.text)
