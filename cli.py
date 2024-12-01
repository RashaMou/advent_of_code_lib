import click
from datetime import datetime
from lib.template_generator import TemplateGenerator

tg = TemplateGenerator()


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
    pass


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
def config(set_token, view):
    """Set or view config"""
    pass


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


if __name__ == "__main__":
    cli()
