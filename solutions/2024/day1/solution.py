from lib.utils import parse_pairs


def solve_part1(input_data):
    pairs = parse_pairs(input_data)
    column1 = []
    column2 = []

    sums = 0

    for pair in pairs:
        column1.append(pair[0])
        column2.append(pair[1])

    while column1:
        smallest1 = min(column1)
        smallest2 = min(column2)

        sums = sums + abs(smallest1 - smallest2)
        column1.remove(smallest1)
        column2.remove(smallest2)

    return sums


def solve_part2(input_data):
    pairs = parse_pairs(input_data)
    column2 = []
    sum = 0

    for pair in pairs:
        column2.append(pair[1])

    for pair in pairs:
        count = column2.count(pair[0])
        sum = sum + (pair[0] * count)

    return sum


if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            input_data = file.read().strip()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        exit(1)

    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))
