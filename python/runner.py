#!/usr/bin/env python

import sys
import importlib

if __name__ == "__main__":
    day = sys.argv[1]
    solution = importlib.import_module(f"day{day}.solution")
    try:
        input_file = sys.argv[3]
    except IndexError:
        input_file = "full"

    with open(f"../inputs/{day}/{input_file}") as file:
        input = file.read().strip()

    if sys.argv[2] == "1":
        print(solution.part1(input))
    elif sys.argv[2] == "2":
        print(solution.part2(input))
