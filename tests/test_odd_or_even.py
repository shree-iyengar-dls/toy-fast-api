import pytest

from toy_fast_api.odd_or_even import odd_or_even_test


@pytest.mark.parametrize(
    "input_number, expected",
    [(5, "Odd"), (2, "Even")],
)
def test_odd_or_even_test(input_number: int, expected: str):
    assert odd_or_even_test(input_number) == expected
