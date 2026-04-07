from typing import Annotated

import typer

from toy_fast_api.main import odd_or_even, start

from . import __version__

cli_app = typer.Typer()


def version_callback(value: bool):
    if value:
        print(f"Version: {__version__}")
        raise typer.Exit()


@cli_app.callback()
def callback(
    version: Annotated[
        bool | None, typer.Option("--version", callback=version_callback)
    ] = None,
):
    pass


@cli_app.command()
def run_fast_api():
    start()


@cli_app.command()
def check(n: int):
    print(odd_or_even(n))
