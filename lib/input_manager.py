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

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(f"{self.base_path}/{year}/day{day}/input.txt", "w") as f:
            f.write(response.text)

    def get_test_input(self, year, day):
        url = f"https://adventofcode.com/{year}/day/{day}"
        headers = {"Cookie": f"session={self.session_token}"}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch input: {response.status_code}")

        soup = BeautifulSoup(response.content, "html.parser")

        test_input = soup.find("pre").text.strip()

        with open(f"{self.base_path}/{year}/day{day}/test_input.txt", "w") as f:
            f.write(test_input)
