# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("hue, expected", [
    (0.0, 0.0),
    (90.0, 0.25),
    (180.0, 0.5),
    (270.0, 0.75),
    (360.0, 1.0),
])
def test_convert_oklch_to_srgb(hue: float, expected: float) -> None:
    assert helper.convert.oklch_to_srgb(hue) == expected
