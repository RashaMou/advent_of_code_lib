from typing import Any, Tuple
import time
from lib.utils import load_solution
from lib.utils import read_input


class SolutionRunner:
    def __init__(self) -> None:
        pass

    def measure_execution_time(self, func, *args):
        """
        Measure the execution time of a function
        """
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        return result, end_time - start_time

    def run_solution(self, year: int, day: int) -> Tuple[Any, Any]:
        """
        Run the solution for a specific year and day.

        Returns:
            Tuple[Any, Any]: The results of Part 1 and Part 2.
        """
        module = load_solution(year, day)
        input_data = read_input(year, day)

        part1_result, part1_time = self.measure_execution_time(
            module.solve_part1, input_data
        )

        part2_result, part2_time = self.measure_execution_time(
            module.solve_part2, input_data
        )

        return (part1_result, part1_time), (part2_result, part2_time)
