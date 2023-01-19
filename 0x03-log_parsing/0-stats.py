#!/usr/bin/python3
import sys

lines_count = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        parts = line.split(" ")
        if len(parts) != 9:
            continue
        ip, date, request, status, size = parts[0], parts[3], parts[5], int(parts[8]), int(parts[9])

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
    print("File size:", total_size)
    for status, count in sorted(status_codes.items()):
        if count > 0:
