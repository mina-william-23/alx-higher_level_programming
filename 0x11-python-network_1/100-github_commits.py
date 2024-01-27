#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""


if __name__ == "__main__":
    import requests
    import sys
    user = sys.argv[2]
    repo = sys.argv[1]
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    headers = {"Accept": "application/vnd.github.v3+json",
               "X-GitHub-Api-Version": "2022-11-28",
               }
    response = requests.get(url, headers=headers)
    body = response.json()
    body = body[:10]
    for commit in body:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(sha, author, sep=": ")
