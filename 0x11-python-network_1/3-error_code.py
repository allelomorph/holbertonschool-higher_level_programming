#!/usr/bin/python3
"""0x11. Python - Network #1, task 3. Error code #0
"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
        print(html.decode(response.headers.get_content_charset()))
    except error.URLError as err:
        print('Error code: {}'.format(err.code))
