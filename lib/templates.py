SOLUTION_TEMPLATE = """def solve_part1(input_data):
    # TODO: Implement solution for Part 1
    pass

def solve_part2(input_data):
    # TODO: Implement solution for Part 2
    pass

if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            input_data = file.read().strip()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        exit(1)

    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))
"""

TEST_TEMPLATE = """from lib.utils import load_solution, read_input

EXAMPLE_INPUT = read_input({year}, {day}, test=True) 
EXPECTED_OUTPUT_PART1 = ""
EXPECTED_OUTPUT_PART2 = ""
module = load_solution({year}, {day})

def test_solve_part1():
    assert module.solve_part1(EXAMPLE_INPUT) == EXPECTED_OUTPUT_PART1

def test_solve_part2():
    assert module.solve_part2(EXAMPLE_INPUT) == EXPECTED_OUTPUT_PART2
"""
