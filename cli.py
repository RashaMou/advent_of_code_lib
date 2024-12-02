from typing import Required
import click
import pytest
import json
from datetime import datetime
from lib.template_generator import TemplateGenerator
from lib.input_manager import InputManager
from lib.solution_runner import SolutionRunner
from lib.config import config

tg = TemplateGenerator()
im = InputManager()
runner = SolutionRunner()


def get_current_year():
    return datetime.now().year


def validate_input(year, day):
    try:
        if not (1 <= day <= 25):
            raise ValueError(f"Invalid day: {day}. Day must be between 1 and 25.")
        if len(str(year)) != 4 or not str(year).isdigit():
            raise ValueError(f"Invalid year: {year}. Year must be a 4-digit number.")
    except ValueError as e:
        raise click.BadParameter(f"Validation failed: {e}")


@click.group()
def cli():
    """Advent of code cli tool"""
    pass


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to run (defaults to current year)",
)
@click.option("--day", type=int, required=True, help="The day to run")
def run(year, day):
    """Run solution for a specific day"""
    validate_input(year, day)
    try:
        part1, part2 = runner.run_solution(year, day)
        print(f"Results for Year {year}, Day {day}:")
        print(f"Part 1: {part1[0]} (Execution Time: {part1[1]:.4f}s)")
        print(f"Part 2: {part2[0]} (Execution Time: {part2[1]:.4f}s)")
    except FileNotFoundError as e:
        click.echo(f"Error: {e}. Make sure you have initialized or fetched inputs.")
    except PermissionError as e:
        click.echo(f"Permission Error: {e}. Check directory permissions.")
    except Exception as e:
        print(f"Error: {e}")


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to test (defaults to current year)",
)
@click.option("--day", type=int, required=True, help="The day to test")
@click.option(
    "--part", type=int, required=False, help="Specify the part to test: 1 or 2"
)
def test(year, day, part):
    """Run test for a specific day"""
    try:
        pytest_args = [
            f"solutions/{year}/day{day}/test_solution.py",
            "-v",
        ]

        if part == 1:
            pytest_args.extend(["-k", "test_solve_part1"])
        elif part == 2:
            pytest_args.extend(["-k", "test_solve_part2"])

        result = pytest.main(pytest_args)

        if result == 0:
            click.echo(f"All tests passed for Year {year}, Day {day}.")
        else:
            click.echo(f"Some tests failed for Year {year}, Day {day}.")
    except Exception as e:
        click.echo(f"Error while running tests: {e}")


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to display status (defaults to current year)",
)
def status(year):
    """Display the completion status for a specific year"""
    click.echo("Not yet implemented")


@cli.command()
@click.option("--set-token", type=str, help="Set the session token from AOC")
@click.option("--view", is_flag=True, help="View config settings")
def config_file(set_token, view):
    """Set or view config"""
    if set_token:
        if not set_token.strip():
            click.echo("Error: Session token cannot be empty")
            return

        config["session_token"] = set_token

        try:
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)

            click.echo("Session token updated successfully")
        except IOError as e:
            click.echo(f"Error writing to config file: {e}")

    if view:
        click.echo(f"Session token: {config.get('session_token', 'Not set')}")
        click.echo(f"Base path: {config.get('base_path', 'Not set')}")


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to initialize (defaults to current year)",
)
@click.option("--day", type=int, required=True, help="The day to initialize")
def init(year, day):
    """Initialize a new puzzle"""
    validate_input(year, day)
    click.echo(f"Initializing day {day} for year {year}")
    tg.create_day_structure(year, day)


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to fetch (defaults to current year)",
)
@click.option("--day", type=int, required=True, help="The day to fetch")
def fetch(year, day):
    """Fetch a day's puzzle input"""
    validate_input(year, day)

    try:
        click.echo(f"Fetching input for day {day} of year {year}")
        im.get_input(year, day)
        im.get_test_input(year, day)
        click.echo("Fetch successful")
    except ValueError as e:
        click.echo(f"Configuration Error: {e}. Check your session token or base path.")
    except PermissionError as e:
        click.echo(f"Permission Error: {e}. Check directory permissions.")
    except Exception as e:
        click.echo(f"Unexpected Error: {e}")


if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
