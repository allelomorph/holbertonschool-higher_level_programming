#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 16. Log parsing"""


if __name__ == '__main__':
    import sys
    from collections import OrderedDict

    line_no = 0
    total_file_size = 0
    code_counts = OrderedDict.fromkeys([200, 301, 400, 401, 403,
                                        404, 405, 500], 0)

    try:
        for line in sys.stdin:
            line_no += 1
            tokens = line.split(' ')
            # checking total tokens
            if len(tokens) != 9:
                continue
            # checking ip address
            ip = tokens[0].split('.')
            for n in ip:
                if not n.isdecimal():
                    continue
            # checking code for dict
            if not tokens[-2].isdecimal():
                continue
            code = int(tokens[-2])
            code_counts[code] += 1
            # checking file size (minus newline)
            if not tokens[-1][:-1].isdecimal():
                continue
            total_file_size += int(tokens[-1])
            if line_no % 10 == 0:
                print("File size: {}".format(total_file_size))
                for code in code_counts:
                    if code_counts[code] > 0:
                        print("{}: {}".format(code, code_counts[code]))
        print("File size: {}".format(total_file_size))
        for code in code_counts:
            if code_counts[code] > 0:
                print("{}: {}".format(code, code_counts[code]))

    except KeyboardInterrupt:
        print("File size: {}".format(total_file_size))
        for code in code_counts:
            if code_counts[code] > 0:
                print("{}: {}".format(code, code_counts[code]))
        raise

"""Example input line:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
128.230.61.246 - [2017-02-05 23:31:23.258076] \
"GET /projects/260 HTTP/1.1" 301 292"""
