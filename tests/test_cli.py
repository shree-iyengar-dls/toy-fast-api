from typer.testing import CliRunner

from toy_fast_api.cli import cli_app

runner = CliRunner()


def test_check_even():
    result = runner.invoke(cli_app, ["check", "2"])
    assert result.exit_code == 0
    assert "'odd_or_even': 'Even'" in result.stdout


def test_check_odd():
    result = runner.invoke(cli_app, ["check", "3"])
    assert result.exit_code == 0
    assert "'odd_or_even': 'Odd'" in result.stdout
