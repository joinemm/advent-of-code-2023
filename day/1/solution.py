import unittest


def part1(input_file):
    total = 0
    with open(input_file) as file:
        for line in file.readlines():
            val = ""
            for i, step in [(0, 1), (len(line) - 1, -1)]:
                while True:
                    try:
                        val += str(int(line[i]))
                        break
                    except ValueError:
                        i += step

            total += int(val)

    return total


def part2(input_file):
    num_strings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    total = 0
    with open(input_file) as file:
        for line in file.readlines():
            found = set()
            for s, v in num_strings.items():
                f = line.find(s)
                if f > -1:
                    found.add((f, v))
                l = line.rfind(s)
                if l > -1:
                    found.add((l, v))

            for i, step in [(0, 1), (len(line) - 1, -1)]:
                while 0 <= i < len(line):
                    try:
                        found.add((i, int(line[i])))
                        break
                    except ValueError:
                        i += step

            found = sorted(found)
            total += found[0][1] * 10 + found[-1][1]

    return total


if __name__ == "__main__":
    print(part1("input"))
    print(part2("input"))
