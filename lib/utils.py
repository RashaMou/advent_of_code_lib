import os
import importlib


def load_solution(year: int, day: int):
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


def read_input(year: int, day: int) -> str:
    """
    Read the input file for a specific year and day.
    """
    input_path = f"solutions/{year}/day{day:02d}/input.txt"
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r") as file:
        return file.read().strip()
