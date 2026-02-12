# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0.0),
        (0.0, 0.0),
        (25, 0.25),
        (25.0, 0.25),
        (50, 0.5),
        (50.0, 0.5),
        (75, 0.75),
        (75.0, 0.75),
        (100, 1.0),
        (100.0, 1.0),
    ],
)
def test_convert_percentage_to_colorsys_decimal(value: float, expected: float) -> None:
    assert helper.convert.percentage_to_colorsys_decimal(value) == expected
