#!/usr/bin/python3
"""0x11. Python - Network #1, task 6. POST an email #1
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    response = post(argv[1], data={'email': argv[2]})
    print(response.text)
