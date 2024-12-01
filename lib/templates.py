SOLUTION_TEMPLATE = """def solve_part1(input_data):
    # TODO: Implement solution for Part 1
    pass

def solve_part2(input_data):
    # TODO: Implement solution for Part 2
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_data = file.read()
    
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))
"""

TEST_TEMPLATE = '''import pytest
from solution import solve_part1, solve_part2

# Example input and expected outputs
EXAMPLE_INPUT = """<INSERT EXAMPLE INPUT>"""
EXPECTED_OUTPUT_PART1 = <INSERT EXPECTED OUTPUT FOR PART 1>
EXPECTED_OUTPUT_PART2 = <INSERT EXPECTED OUTPUT FOR PART 2>

def test_solve_part1():
    assert solve_part1(EXAMPLE_INPUT) == EXPECTED_OUTPUT_PART1

def test_solve_part2():
    assert solve_part2(EXAMPLE_INPUT) == EXPECTED_OUTPUT_PART2
'''
