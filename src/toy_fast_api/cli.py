import typer

from toy_fast_api.main import start

cli_app = typer.Typer()


@cli_app.command()
def run_fast_api():
    start()
