def part1(input_file):
    limits = {"red": 12, "green": 13, "blue": 14}
    possible = []
    with open(input_file) as file:
        for line in file.readlines():
            impossible = False
            id, data = line.strip("Game ").split(":")
            rounds = [x.split(",") for x in data.split(";")]
            for round in rounds:
                for cube in round:
                    n, name = cube.strip().split()
                    if int(n) > limits[name]:
                        impossible = True

            if not impossible:
                possible.append(int(id))

    return sum(possible)


def part2(input_file):
    total = 0
    with open(input_file) as file:
        for line in file.readlines():
            used = {"red": 0, "green": 0, "blue": 0}
            id, data = line.strip("Game ").split(":")
            rounds = [x.split(",") for x in data.split(";")]
            for round in rounds:
                for cube in round:
                    n, name = cube.strip().split()
                    n = int(n)
                    if n > used[name]:
                        used[name] = n
            power = used["red"] * used["green"] * used["blue"]
            total += power

    return total


if __name__ == "__main__":
    print(part1("input"))
    print(part2("input"))
