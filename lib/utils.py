import os
import importlib
from bs4 import BeautifulSoup
import requests
from lib.config import config
from typing import Tuple, Any


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


def read_input(year: int, day: int, test: bool = False) -> str:
    """
    Read the input file for a specific year and day.
    """
    if test:
        input_path = f"solutions/{year}/day{day}/test_input.txt"
    else:
        input_path = f"solutions/{year}/day{day}/input.txt"
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r") as file:
        return file.read().strip()


def parse_arrays(data) -> []:
    """
    Parse space separated rows of numbers into a list of arrays
    """
    arr = []
    for line in data.strip().split("\n"):
        arr.append(line.split(" "))

    return arr


def parse_pairs(data) -> Tuple[Any, Any]:
    """
    Parse space-separated pairs of numbers into list of tuples.

    Args:
        data (str): Multiline string with space-separated numbers

    Returns:
        list[tuple[int, int]]: List of number pairs as tuples
    """
    pairs = []

    for line in data.strip().split("\n"):
        x, y = map(int, line.split())
        pairs.append((x, y))

    return pairs


def get_status(year) -> None:
    if not config["session_token"]:
        raise ValueError("Session token is required")

    url = f"https://adventofcode.com/{year}"
    headers = {"Cookie": f"session={config["session_token"]}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.HTTPError as e:
        if response.status_code == 401:
            raise PermissionError(
                "Unauthorized: Check if your session token is valid."
            ) from e
        elif response.status_code == 404:
            raise FileNotFoundError(f"Input not found for Year {year}.") from e
        else:
            raise ConnectionError(
                f"HTTP Error {response.status_code}: {response.reason}"
            ) from e
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to connect to Advent of Code: {e}") from e

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        calendar = soup.find("pre", class_="calendar")

        if not calendar:
            raise ValueError("Calendar not found in the HTML content.")

        days = calendar.find_all("a")

        for i, day in enumerate(days):
            if "calendar-verycomplete" in day.get("class", []):
                print(f"Day {i + 1}: 🤩 🤩")
            elif "calendar-complete" in day.get("class", []):
                print(f"Day {i + 1}: 🤩")
            else:
                print(f"Day {i + 1}: 💩")
    except Exception as e:
        raise Exception(f"Error parsing HTML: {e}")
