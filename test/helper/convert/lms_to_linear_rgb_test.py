# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("long, medium, short, expected", [
    (0.0, 0.0, 0.0, (0.0, 0.0, 0.0)),  # Test black: zero for all LMS values.
    (1.0, 1.0, 1.0, (1.0, 1.0, 1.0)),  # Test white: all LMS values are 1.
    (1.0, 0.0, 0.0, (4.0767416621, -1.2684380046, -0.0041960863)),  # Test pure long (reddish-yellow cone response).
    (0.0, 1.0, 0.0, (-3.3077115913, 2.6097574011, -0.7034186147)),  # Test pure medium (greenish cone response).
    (0.5, 0.5, 0.5, (0.5, 0.5, 0.5)),  # Test mid-grey: all LMS values are 0.5.
])
def test_convert_lms_to_linear_rgb(long: float, medium: float, short: float, expected: tuple[float, float, float]) -> None:
    assert helper.convert.lms_to_linear_rgb(long, medium, short) == expected
