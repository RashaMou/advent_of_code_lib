import os
from lib.templates import SOLUTION_TEMPLATE, TEST_TEMPLATE
from lib.utils import Utilities

utils = Utilities()


class TemplateGenerator:
    def __init__(self):
        self.config = utils.load_config()
        self.base_path = self.config["base_path"]

    def create_day_structure(self, year: int, day: int) -> str:
        """
        Create the directory structure for a specific year and day.

        Returns:
            str: The path to the created day directory.
        """
        does_exist = self.check_existing_day(year, day)
        if does_exist:
            return f"Files exist for {year}-{day}"

        day_path = f"{self.base_path}/{year}/day{day}"
        os.makedirs(day_path)

        self.generate_files_for_day(day_path)

    def generate_files_for_day(self, path: str) -> None:
        """
        Generate all necessary files for a specific day using templates.
        """
        templates = self.load_templates()

        for key, value in templates.items():
            with open(f"{path}/{key}", "w") as key:
                key.write(value)

        with open(f"{path}/input.txt", "w"):
            pass

        with open(f"{path}/test_input.txt", "w"):
            pass

    def load_templates(self) -> dict:
        """
        Load the predefined templates for files.

        Returns:
            dict: A dictionary containing file names as keys and template content as values.
        """
        return {
            "solution.py": SOLUTION_TEMPLATE,
            "test_solution.py": TEST_TEMPLATE,
        }

    def check_existing_day(self, year: int, day: int) -> bool:
        """
        Check if the directory and necessary files for a day already exist.
        """
        return os.path.exists(f"{self.base_path}/{year}/day{day}")
