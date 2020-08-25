#!/usr/bin/python3
"""0x11. Python - Network #1, task 9. My Github!
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/user'
    # builtin shorthand for auth=requests.auth.HTTPBasicAuth('user', 'pass')
    response = get(url, auth=(argv[1], argv[2]))
    print(response.json().get('id'))
