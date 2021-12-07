#!/usr/bin/env python3
"""
Author: Charles De Mount <thexrayone@icloud.com>
Purpose: Say hello
"""
import argparse
from os import confstr
import sys

file = "./input.txt"

# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find keys", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "input",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        help="Input file",
    )

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Find the number of value increases"""

    args = get_args()

    input_list = [int(line.rstrip("\n")) for line in args.input]

    previous_frame, depth_count = 0, 0

    for index in range(len(input_list) - 2):
        current_frame = sum(input_list[index : index + 3])
        if index > 0 and current_frame > previous_frame:
            depth_count += 1
        previous_frame = current_frame

    print(depth_count)


if __name__ == "__main__":
    main()
