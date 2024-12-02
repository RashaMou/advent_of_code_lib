from lib.utils import load_solution, read_input

EXAMPLE_INPUT = read_input(2024, 1, test=True)
EXPECTED_OUTPUT_PART1 = 11
EXPECTED_OUTPUT_PART2 = 31
module = load_solution(2024, 1)


def test_solve_part1():
    assert module.solve_part1(EXAMPLE_INPUT) == EXPECTED_OUTPUT_PART1


def test_solve_part2():
    assert module.solve_part2(EXAMPLE_INPUT) == EXPECTED_OUTPUT_PART2
