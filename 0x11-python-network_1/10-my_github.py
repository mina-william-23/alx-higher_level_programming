#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access
token as password)
"""


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    # url = 'https://api.github.com/user'
    # headers = {"Accept": "application/vnd.github.v3+json",
    #          "X-GitHub-Api-Version": "2022-11-28",
    #           "Authorization": f"Bearer {password}"
    #           }
    # response = requests.get(url, headers=headers)
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(username, password), timeout=5)
    print(res.json().get('id'))
