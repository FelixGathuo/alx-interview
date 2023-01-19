#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """
import sys

lines_count = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
""" Trys this block """
    for line in sys.stdin:
    """ Split lines """
        parts = line.split(" ")
        if len(parts) != 9:
            continue
        ip, date, request = parts[0], parts[3], parts[5]
        status, size = int(parts[8]), int(parts[9])

        if status not in status_codes:
            continue
        status_codes[status] += 1
        total_size += size
        lines_count += 1

        if lines_count % 10 == 0:
            print("File size:", total_size)
            for status, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{status}: {count}")
except KeyboardInterrupt:
""" In case keyoard is pressed """
    print("File size:", total_size)
    for status, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{status}: {count}")
