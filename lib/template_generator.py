import os
from lib.templates import SOLUTION_TEMPLATE, TEST_TEMPLATE
from lib.config import config


class TemplateGenerator:
    def __init__(self):
        self.base_path = config["base_path"]

    def create_day_structure(self, year: int, day: int) -> str:
        """
        Create the directory structure for a specific year and day.

        Returns:
            str: The path to the created day directory.
        """
        day_path = self.generate_day_path(year, day)

        does_exist = self.check_existing_day(year, day)

        if does_exist:
            raise FileExistsError(
                f"Files for Year {year}, Day {day} already exist at '{day_path}'."
            )

        try:
            os.makedirs(day_path)
        except OSError as e:
            raise OSError(f"Failed to create directory '{day_path}': {e}")

        self.generate_files_for_day(year, day)

    def generate_day_path(self, year, day):
        return f"{self.base_path}/{year}/day{day}"

    def generate_files_for_day(self, year: int, day: int) -> None:
        """
        Generate all necessary files for a specific day using templates.
        """
        templates = self.load_templates()
        path = self.generate_day_path(year, day)

        for file_name, template_content in templates.items():
            try:
                with open(f"{path}/{file_name}", "w") as file:
                    if file_name == "test_solution.py":
                        file.write(template_content.format(year=year, day=day))
                    else:
                        file.write(template_content)

            except IOError as e:
                raise IOError(f"Failed to write file to '{file_name}' to '{path}': {e}")

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
