#!/usr/bin/python3
"""0x11. Python - Network #1, task 8. Search API
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    q = '' if len(argv) < 2 else argv[1]
    response = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = response.json()
    except ValueError:
        print('No result' if response.status_code == 204
              else 'Not a valid JSON')
    else:
        print('No result' if len(json_dict) == 0
              else '[{}] {}'.format(json_dict.get('id'),
                                    json_dict.get('name')))
