import json
import requests


class InputManager:
    def __init__(self, config_path: str = "config.json"):
        self.config = config_path
        self.session_token = ""
        self.base_path = ""

    def load_config(self, config) -> None:
        with open(self.config, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.session_token = data["session_token"]
            self.solutions_path = data["solutions_path"]

    def get_input(self, year, day) -> None:
        with open(self.config, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.session_token = data["session_token"]

        if not self.session_token:
            raise ValueError("Session token is required")

        url = f"https://adventofcode.com/{year}/day/{day}/input"

        headers = {"Cookie": f"session={self.session_token}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(f"{self.base_path}/{year}/day{day}/input.txt", "w") as f:
            f.write(response.text)

    def get_test_input(self):
        pass
