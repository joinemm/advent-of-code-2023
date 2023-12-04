def part1(input: str):
    points = 0
    for line in input.split("\n"):
        winners, numbers = [set(x.split()) for x in line.split(":", 1)[1].split("|", 1)]
        if matches := numbers.intersection(winners):
            points += 2 ** (len(matches) - 1)

    return points


def part2(input: str):
    lines = input.split("\n")
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        winners, numbers = [set(x.split()) for x in line.split(":", 1)[1].split("|", 1)]
        for n in range(len(numbers.intersection(winners))):
            cards[i + n + 1] += cards[i]

    return sum(cards)
