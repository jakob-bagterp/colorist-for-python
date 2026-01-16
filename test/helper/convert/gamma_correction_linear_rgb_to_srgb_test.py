# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("red, green, blue, expected", [
    (0.0, 0.0, 0.0, (0, 0, 0)),
    (0.5, 0.5, 0.5, (187, 187, 187)),
    (1.0, 1.0, 1.0, (255, 255, 255)),
    (0.25, 0.5, 0.75, (136, 187, 224)),
    (0.1, 0.2, 0.3, (89, 123, 148)),
])
def test_convert_gamma_correction_linear_rgb_to_srgb(red: float, green: float, blue: float, expected: tuple[int, int, int]) -> None:
    assert helper.convert.gamma_correction_linear_rgb_to_srgb(red, green, blue) == expected
