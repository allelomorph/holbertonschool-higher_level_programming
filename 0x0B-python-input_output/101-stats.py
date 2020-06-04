#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 16. Log parsing"""


def main():
    """Reads stdin line by line and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>

    """
    import sys
    import os
    from collections import OrderedDict

    path = '101-log.txt'

    if os.path.exists(path):
        os.remove(path)

    line_no = 0

    code_counts = OrderedDict()
    code_counts['200'] = 0
    code_counts['301'] = 0
    code_counts['400'] = 0
    code_counts['401'] = 0
    code_counts['403'] = 0
    code_counts['404'] = 0
    code_counts['405'] = 0
    code_counts['500'] = 0

    try:
        while True:
            with open(path, 'a', encoding='utf-8') as log:
                for line in sys.stdin:
                    line_no += 1
                    log.write(line)
                    tokens = line.split(' ')
                    code = tokens[-2]
                    code_counts[code] += 1
                    if line_no % 10 == 0:
                        break
            if line_no % 10 == 0:
                print("File size: {}".format(os.path.getsize('./' + path)))
                for code in code_counts:
                    if code_counts[code] > 0:
                        print("{}: {}".format(code, code_counts[code]))

    except KeyboardInterrupt:
        print("File size: {}".format(os.path.getsize('./' + path)))
        for code in code_counts:
            if code_counts[code] > 0:
                print("{}: {}".format(code, code_counts[code]))
        log.close()
        raise

if __name__ == '__main__':
    main()
