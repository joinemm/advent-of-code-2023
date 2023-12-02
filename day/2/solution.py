import re


def part1(input_file):
    total = 0
    limits = {"red": 12, "green": 13, "blue": 14}
    with open(input_file) as file:
        for i, line in enumerate(file.readlines(), start=1):
            if False not in map(
                lambda m: int(m.group(1)) <= limits[m.group(2)],
                re.finditer(r"(\d*) (blue|red|green)", line),
            ):
                total += i

    return total


def part2(input_file):
    total = 0
    with open(input_file) as file:
        for line in file.readlines():
            power = 1
            matches = re.findall(r"(\d*) (red|green|blue)", line)
            for color in ["red", "green", "blue"]:
                power *= max(
                    [int(m[0]) for m in filter(lambda m: m[1] == color, matches)]
                )

            total += power

    return total


if __name__ == "__main__":
    print(part1("input"))
    print(part2("input"))
