import sys
from xmlrpc.client import MAXINT


def main(file_name):
    # print(f'Param {file}')
    file = open(file_name)
    previous_input = MAXINT
    incrementing_count = 0
    for line in file:
        value = int(line)
        if value > previous_input:
            incrementing_count += 1
        previous_input = value

    print(f'Count: {incrementing_count}')


if __name__ == '__main__':
    if sys.argv[1] != None:
        main(sys.argv[1])
