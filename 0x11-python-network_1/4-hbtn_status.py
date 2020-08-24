#!/usr/bin/python3
"""0x11. Python - Network #1, task 4. What's my status? #1
"""

if __name__ == "__main__":
    from requests import get

    response = get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
