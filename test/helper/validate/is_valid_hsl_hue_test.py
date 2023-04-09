# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("input, expected", [
    (0, True),
    (100, True),
    (360, True),
    (0.0, True),
    (360.0, True),
    (360.1, False),
    (361, False),
    (-1, False),
])
def test_is_valid_hsl_hue(input: float, expected: bool) -> None:
    assert helper.validate.is_valid_hsl_hue(input) is expected
