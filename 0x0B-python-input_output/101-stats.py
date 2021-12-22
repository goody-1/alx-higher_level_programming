#!/usr/bin/python3
"""
Demonstrates Log parsing

script that reads stdin line by line and computes metrics:

    -   Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        <status code> <file size>
    -   Each 10 lines and after a keyboard interruption (CTRL + C), prints
        those statistics since the beginning:
        -   Total file size: File size: <total size>
        -   where is the sum of all previous (see input format above)
        -   Number of lines by status code:
            -   possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            -   if a status code doesn’t appear, don’t print anything for this
                status code
            -   format: <status code>: <number>
            -   status codes should be printed in ascending order
"""
if __name__ == '__main__':

    import sys

    file_size = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in valid_codes}
    counter = 0

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if counter % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)
    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
