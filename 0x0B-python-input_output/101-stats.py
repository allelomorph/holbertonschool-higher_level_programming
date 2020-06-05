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
            code = int(tokens[-2])
            code_counts[code] += 1
            total_file_size += int(tokens[-1])
            if line_no % 10 == 0:
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
