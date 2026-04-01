import typer

from toy_fast_api.main import odd_or_even, start

cli_app = typer.Typer()


@cli_app.command()
def run_fast_api():
    start()


@cli_app.command()
def check(n: int):
    print(odd_or_even(n))
