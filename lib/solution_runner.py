from typing import Any, Tuple
from datetime import time
import importlib.util
import os


class SolutionRunner:
    def __init__(self) -> None:
        pass

    def load_solution(self, year: int, day: int):
        """
        Dynamically load the solution module for a given year and day.
        """
        path = f"solutions/{year}/day{day}/solution.py"

        if not os.path.exists(path):
            raise FileNotFoundError(f"Solution file not found: {path}")

        try:
            spec = importlib.util.spec_from_file_location("solution", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            raise ImportError(f"Failed to load solution module: {e}")

        if not hasattr(module, "solve_part1") or not hasattr(module, "solve_part2"):
            raise AttributeError(
                f"Module {path} must define 'solve_part1' and 'solve_part2'"
            )

        return module

    def read_input(self, year: int, day: int) -> str:
        """
        Read the input file for a specific year and day.
        """
        input_path = f"solutions/{year}/day{day:02d}/input.txt"
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        with open(input_path, "r") as file:
            return file.read().strip()

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
        module = self.load_solution(year, day)
        input_data = self.read_input(year, day)

        part1_result, part1_time = self.measure_execution_time(
            module.solve_part1, input_data
        )

        part2_result, part2_time = self.measure_execution_time(
            module.solve_part2, input_data
        )

        return (part1_result, part1_time), (part2_result, part2_time)
