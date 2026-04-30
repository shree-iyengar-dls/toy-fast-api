from typing import Annotated

import typer

from toy_fast_api.config import ApplicationConfig, CustomOIDC
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
    start(
        ApplicationConfig(
            oidc=CustomOIDC(
                well_known_url="https://identity-test.diamond.ac.uk/realms/dls/.well-known/openid-configuration",
                client_id="ToyFastAPI",
                client_audience="account",
            )
        )
    )


@cli_app.command()
def check(n: int):
    print(odd_or_even(n))
