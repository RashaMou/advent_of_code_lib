from lib.utils import parse_arrays


def solve_part1(input_data):
    safe = 0
    arrs = parse_arrays(input_data)

    for arr in arrs:
        if is_increasing(arr):
            safe += 1
        elif is_decreasing(arr):
            safe += 1

    return safe


def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return False
        if not 1 <= abs(int(arr[i]) - int(arr[i + 1])) <= 3:
            return False
        if int(arr[i]) > int(arr[i + 1]):
            return False
    return True


def is_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return False
        if not 1 <= abs(int(arr[i]) - int(arr[i + 1])) <= 3:
            return False
        if int(arr[i]) < int(arr[i + 1]):
            return False
    return True


def solve_part2(input_data):
    safe = 0
    arrs = parse_arrays(input_data)

    for arr in arrs:
        if is_increasing_with_dampener(arr):
            print(f"Array is increasing: {arr}")
            safe += 1
        elif is_decreasing_with_dampener(arr):
            print(f"Array is decreasing: {arr}")
            safe += 1
        else:
            print(f"Array is not safe: {arr}")

    print(f"number of safes: {safe}")
    return safe


def is_increasing_with_dampener(arr):
    if is_increasing(arr):
        return True

    for i in range(len(arr) - 1):
        equals = arr[i] == arr[i + 1]
        between = 1 <= abs(int(arr[i]) - int(arr[i + 1])) <= 3
        greater = int(arr[i]) > int(arr[i + 1])

        if equals or not between or greater:
            # remove and recheck
            removed_first = arr[0:i] + arr[i + 1 :]
            removed_second = arr[0 : i + 1] + arr[i + 2 :]
            if is_increasing(removed_first) or is_increasing(removed_second):
                return True
    return False


def is_decreasing_with_dampener(arr):
    if is_decreasing(arr):
        return True

    for i in range(len(arr) - 1):
        equals = arr[i] == arr[i + 1]
        between = 1 <= abs(int(arr[i]) - int(arr[i + 1])) <= 3
        less = int(arr[i]) < int(arr[i + 1])

        if equals or not between or less:
            removed_first = arr[0:i] + arr[i + 1 :]
            removed_second = arr[0 : i + 1] + arr[i + 2 :]
            if is_decreasing(removed_first) or is_decreasing(removed_second):
                return True
    return False


if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            input_data = file.read().strip()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        exit(1)

    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))
