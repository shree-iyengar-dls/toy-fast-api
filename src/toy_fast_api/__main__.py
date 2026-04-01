"""Interface for ``python -m toy_fast_api``."""

from toy_fast_api.cli import cli_app

__all__ = ["main"]


def main():
    cli_app()


if __name__ == "__main__":
    main()
