import re


def part1(input: str):
    total = 0
    limits = {"red": 12, "green": 13, "blue": 14}
    for i, line in enumerate(input.split("\n"), start=1):
        if False not in map(
            lambda m: int(m[0]) <= limits[m[1]],
            re.findall(r"(\d*) (blue|red|green)", line),
        ):
            total += i

    return total


def part2(input: str):
    total = 0
    for line in input.split("\n"):
        power = 1
        matches = re.findall(r"(\d*) (red|green|blue)", line)
        for color in ["red", "green", "blue"]:
            power *= max([int(m[0]) for m in filter(lambda m: m[1] == color, matches)])

        total += power

    return total
