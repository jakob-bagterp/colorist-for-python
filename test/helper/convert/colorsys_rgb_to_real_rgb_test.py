# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "rgb_colorsys, expected",
    [
        ((0.5, 0.5, 0.5), (127, 127, 127)),
        ((0.0, 0.0, 0.0), (0, 0, 0)),
        ((1.0, 1.0, 1.0), (255, 255, 255)),
        ((0.25, 0.75, 0.5), (63, 191, 127)),
        ((0.33, 0.66, 0.99), (84, 168, 252)),
        ((0.1, 0.9, 0.5), (25, 229, 127)),
        ((0.255, 0.512, 0.768), (65, 130, 195)),
    ],
)
def test_convert_colorsys_rgb_to_real_rgb(
    rgb_colorsys: tuple[float, float, float], expected: tuple[int, int, int]
) -> None:
    assert helper.convert.colorsys_rgb_to_real_rgb(rgb_colorsys) == expected
