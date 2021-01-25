#!/usr/bin/python3
"""
0x0B. Python - Input/Output, task 16. Log parsing

Parses a log of HTTP GET request results from stdin to tabulate the total
counts of status codes appearing in each response, and the total file size
across all requests.

Example of expected log line input:
128.230.61.246 - [2017-02-05 23:31:23.258076] \
"GET /projects/260 HTTP/1.1" 301 292

Fields:
<IP Address> - [<date>] "<GET request>" <response status code> <file size>
"""


def print_log_totals(total_file_size, code_counts):
    """
    Prints current totals of file size and status code counts.

    Args:
        total_file_size (int): cumulative total of bytes received through
            GET requests in log
        code_counts (OrderedDict): totals of status codes from repsonses
    """
    print("File size: {}".format(total_file_size))
    for code in code_counts:
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


if __name__ == '__main__':
    from sys import argv, stdin, stderr
    from collections import OrderedDict
    from datetime import datetime

    line_no = 0
    total_file_size = 0
    code_counts = OrderedDict.fromkeys([200, 301, 400, 401, 403,
                                        404, 405, 500], 0)

    try:
        for line in stdin:
            line_no += 1

            # both ip addresses/URLs allowed, but some lines may be raw text
            a = line.split('-', 1)
            if len(a) != 2:
                # likely not a formatted line
                continue

            # checking timestamp
            b = a[1].split(']')
            timecode = b[0].lstrip(' [')
            try:
                datetime.strptime(timecode, '%Y-%m-%d %H:%M:%S.%f')
            except:
                stderr.write("{}: {}: invalid timecode\n".format(
                    argv[0], line_no))
                pass

            # checking URL
            c = b[1].split('"')
            c = c[1:]
            if c[0] != 'GET /projects/260 HTTP/1.1':
                stderr.write("{}: {}: unexpected HTTP request\n".format(
                    argv[0], line_no))

            # prep for status code and file size
            d = c[1].lstrip(' ')
            d = d.rstrip('\n')
            d = d.split(' ')

            # checking status code (invalid codes skipped without error)
            if d[0].isdecimal():
                code = int(d[0])
                code_counts[code] += 1

            # checking file size (invalid sizes skipped without error)
            if d[1].isdecimal():
                total_file_size += int(d[1])

            if line_no % 10 == 0:
                print_log_totals(total_file_size, code_counts)
        print_log_totals(total_file_size, code_counts)

    except (KeyboardInterrupt):
        print_log_totals(total_file_size, code_counts)
        raise
