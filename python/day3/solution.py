import re


def part1(input: str):
    total = 0
    lines = [line + '.' for line in input.split("\n")]
    h = len(lines)
    w = len(lines[0])
    for y in range(h):
        number_buffer = ""
        for x in range(w):
            if (c := lines[y][x]).isdigit():
                number_buffer += c
                continue

            if number_buffer:
                for j in range(len(number_buffer) + 2):
                    for jy in range(-1 if y > 0 else 0, 2 if y < h - 1 else 1):
                        s = lines[y + jy][x - j]
                        if not s.isdigit() and s != ".":
                            total += int(number_buffer)
                            break
                    else:
                        continue
                    break
                number_buffer = ""

    return total


def part2(input: str):
    total = 0
    lines = input.split("\n")
    w = len(lines[0])
    for y in range(len(lines)):
        x = 0
        while True:
            if (x := lines[y].find("*", x + 1)) == -1:
                break

            numbers = []
            for y_delta in [-1, 0, 1]:
                area = [lines[y + y_delta][x]]
                for step in [-1, 1]:
                    i = x
                    while i < w - 1:
                        i += step
                        nc = lines[y + y_delta][i]
                        if nc.isdigit():
                            area.insert(0 if step == -1 else len(area), nc)
                        else:
                            break

                numbers += re.findall(r"\d+", "".join(area))

            if len(numbers) == 2:
                total += int(numbers[0]) * int(numbers[1])

    return total
