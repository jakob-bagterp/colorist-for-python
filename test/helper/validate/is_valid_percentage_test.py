# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("input, expected", [
    (0, True),
    (56, True),
    (100, True),
    (0.0, True),
    (100.0, True),
    (100.1, False),
    (101, False),
    (-1, False),
])
def test_is_valid_percentage(input: float, expected: bool) -> None:
    assert helper.validate.is_valid_percentage(input) is expected
