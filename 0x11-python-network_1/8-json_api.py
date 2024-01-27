#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""


if __name__ == "__main__":
    import requests
    import sys

    value = ""
    if len(sys.argv) > 1:
        value = sys.argv[1]
    data = {"q": value}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_res = response.json()
        if json_res:
            print("[{}] {}".format(json_res['id'], json_res['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
