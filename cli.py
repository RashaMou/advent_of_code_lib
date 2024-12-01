import click
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


@click.group()
def cli():
    """Advent of code cli tool"""
    pass


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to debug (defaults to current year)",
)
@click.option("--day", type=int, required=True, help="The day to debug")
def debug(year, day):
    """Debug the solution for a specific day"""
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
    try:
        part1, part2 = runner.run_solution(year, day)
        print(f"Results for Year {year}, Day {day}:")
        print(f"Part 1: {part1[0]} (Execution Time: {part1[1]:.4f}s)")
        print(f"Part 1: {part2[0]} (Execution Time: {part2[1]:.4f}s)")
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
def test(year, day):
    """Run test for a specific day"""
    pass


@cli.command()
@click.option(
    "--year",
    type=int,
    default=get_current_year,
    help="The year to display status (defaults to current year)",
)
def status(year):
    """Display the completion status for a specific year"""
    pass


@cli.command()
@click.option("--set-token", type=str, help="Set the session token from AOC")
@click.option("--view", is_flag=True, help="View config settings")
def config_file(set_token, view):
    """Set or view config"""
    if set_token:
        config["session_token"] = set_token

        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)

        click.echo("Session token updated successfully")

    if view:
        print(f"Session token: {config['session_token']}")
        print(f"Base path: {config['base_path']}")


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
    click.echo(f"Fetching input for day {day} of year {year}")
    im.get_input(year, day)
    im.get_test_input(year, day)


if __name__ == "__main__":
    cli()
