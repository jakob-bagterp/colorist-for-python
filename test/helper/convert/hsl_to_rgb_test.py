# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "hue, saturation, lightness, expected",
    [
        (0, 100, 50, (255, 0, 0)),
        (120, 100, 50, (0, 255, 0)),
        (240, 100, 50, (0, 0, 255)),
        (60, 100, 50, (254, 255, 0)),
        (180, 100, 50, (0, 254, 255)),
        (300, 100, 50, (255, 0, 254)),
        (360, 100, 50, (255, 0, 0)),
        (0, 0, 0, (0, 0, 0)),
        (0, 0, 100, (255, 255, 255)),
        (0, 0, 50, (127, 127, 127)),
        (210, 50, 50, (63, 127, 191)),
    ],
)
def test_convert_hsl_to_rgb(hue: float, saturation: float, lightness: float, expected: tuple[int, int, int]) -> None:
    assert helper.convert.hsl_to_rgb(hue, saturation, lightness) == expected
