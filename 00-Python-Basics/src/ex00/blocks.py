import argparse
import sys


def print_lines(number_of_lines):
    count = 0
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("00000") and line[5] != "0" and len(line) == 32:
            print(line)
            count += 1
        if count >= number_of_lines:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "number_of_lines", help="display given number of non-corrupted lines", type=int
    )
    args = parser.parse_args()
    print_lines(args.number_of_lines)
