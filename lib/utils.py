import json


class Utilities:
    def __init__(self) -> None:
        self.config = "config.json"

    def load_config(self):
        with open(self.config, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
