import requests
from bs4 import BeautifulSoup
from lib.config import config


class InputManager:
    def __init__(self):
        self.session_token = config["session_token"]
        self.base_path = config["base_path"]

    def get_input(self, year, day) -> None:
        if not self.session_token:
            raise ValueError("Session token is required")

        url = f"https://adventofcode.com/{year}/day/{day}/input"

        headers = {"Cookie": f"session={self.session_token}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.HTTPError as e:
            if response.status_code == 401:
                raise PermissionError(
                    "Unauthorized: Check if your session token is valid."
                ) from e
            elif response.status_code == 404:
                raise FileNotFoundError(
                    f"Input not found for Year {year}, Day {day}."
                ) from e
            else:
                raise ConnectionError(
                    f"HTTP Error {response.status_code}: {response.reason}"
                ) from e
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to connect to Advent of Code: {e}") from e

        try:
            file_path = f"{self.base_path}/{year}/day{day}/input.txt"
            with open(file_path, "w") as f:
                f.write(response.text)
        except IOError as e:
            raise IOError(f"Failed to write input to {file_path}") from e

    def get_test_input(self, year, day):
        if not self.session_token:
            raise ValueError("Session token is required")

        url = f"https://adventofcode.com/{year}/day/{day}"
        headers = {"Cookie": f"session={self.session_token}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.HTTPError as e:
            if response.status_code == 401:
                raise PermissionError(
                    "Unauthorized: Check if your session token is valid."
                ) from e
            elif response.status_code == 404:
                raise FileNotFoundError(
                    f"Input not found for Year {year}, Day {day}."
                ) from e
            else:
                raise ConnectionError(
                    f"HTTP Error {response.status_code}: {response.reason}"
                ) from e
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to connect to Advent of Code: {e}") from e

        try:
            soup = BeautifulSoup(response.content, "html.parser")
            test_input = soup.find("pre")

            if not test_input:
                raise ValueError("Test input not found in the HTML content.")

            test_input = test_input.text.strip()
        except Exception as e:
            raise ValueError(
                f"Failed to parse the test input for Year {year}, Day {day}: {e}"
            ) from e

        try:
            file_path = f"{self.base_path}/{year}/day{day}/test_input.txt"
            with open(file_path, "w") as f:
                f.write(test_input)
        except IOError as e:
            raise IOError(f"Failed to write input to {file_path}") from e
