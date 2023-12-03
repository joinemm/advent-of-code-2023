def read_input(input_file):
    with open(input_file) as file:
        return file.readlines()


def part1(input_file):
    total = 0
    for line in read_input(input_file):
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
    for line in read_input(input_file):
        found = set()
        for s, v in num_strings.items():
            for i in [line.find(s), line.rfind(s)]:
                if i > -1:
                    found.add((i, v))

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
