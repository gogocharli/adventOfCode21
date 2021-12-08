#!/usr/bin/env python3
"""
Author: Charles De Mount <thexrayone@icloud.com>
Purpose: Say hello
"""
import argparse
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

    input_list = [tuple(line.rstrip("\n").split(" ")) for line in args.input]

    aim_scalar = 0
    vec_coords = (0, 0)

    for action, value in input_list:
        value = int(value)
        match action:
            case "forward":
                vec_coords = (vec_coords[0] + value, vec_coords[1] + value * aim_scalar)
            case "down":
                aim_scalar += value
            case "up":
                aim_scalar -= value
            case _:
                print("Should not happen")
    print(f"The current coordinates are {vec_coords}.", end="")
    print(f"Multiplied to {vec_coords[0] * vec_coords[1]}")

if __name__ == "__main__":
    main()
