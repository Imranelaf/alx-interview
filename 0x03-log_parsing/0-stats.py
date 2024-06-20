#!/usr/bin/python3

'''
This script reads from standard input and parses the log file.
It reads the status code and file size from the log file.
It then prints the file size and the number of times each status code was
returned.'''

if __name__ == '__main__':
    from sys import stdin

    counter = 0
    size = 0
    parsed_code = {}

    def print_helper():
        '''
        This function prints the file size and the number of times each status
        code was returned.

        return: None
        '''
        print(f"File size: {size}")
        for code, count in sorted(parsed_code.items()):
            print(f"{code}: {count}")

    try:
        for ln in stdin:
            try:
                linep = ln.split()

                size += int(linep[-1])
                state = int(linep[-2])
                states = [200, 301, 400, 401, 403, 404, 405, 500]
                if state in states:
                    if state in parsed_code:
                        parsed_code[state] += 1
                    else:
                        parsed_code[state] = 1
                    counter += 1

            except (ValueError, IndexError, KeyError, TypeError):
                continue
            else:
                if counter % 10 == 0:
                    print_helper()
        print_helper()
    except KeyboardInterrupt:
        print_helper()
