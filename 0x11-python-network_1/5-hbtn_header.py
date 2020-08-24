#!/usr/bin/python3
"""0x11. Python - Network #1, task 5. Response header value #1
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    print(response.headers.get('x-request-id'))
