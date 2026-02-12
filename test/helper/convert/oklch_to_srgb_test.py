# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "lightness, chroma, hue, expected",
    [
        (0.0, 0.0, 0.0, (0, 0, 0)),  # Neutral black should map to neutral black in sRGB.
        (1.0, 0.0, 180.0, (255, 255, 255)),  # Neutral white should map to neutral white in sRGB.
        (
            0.599,
            0.0,
            0.0,
            (127, 127, 127),
        ),  # Mid-grey where lightness 0.599 is the Oklab/OKLCH value for roughly 50% sRGB.
        (0.628, 0.2577, 29.23, (255, 0, 0)),  # Pure red in sRGB and verified OKLCH coordinates for Hex value #FF0000.
        (
            0.86644,
            0.29483,
            142.5,
            (0, 255, 0),
        ),  # Pure green in sRGB and verified OKLCH coordinates for Hex value #00FF00.
        (0.452, 0.3132, 264.05, (0, 0, 255)),  # Pure blue in sRGB and verified OKLCH coordinates for Hex value #0000FF.
        (0.296, 0.1067, 299.9, (54, 27, 89)),  # Dark purple with Hex value #361B59.
    ],
)
def test_convert_oklch_to_srgb(lightness: float, chroma: float, hue: float, expected: tuple[int, int, int]) -> None:
    """Test conversion from OKLCH color space to sRGB with a tolerance of ±1. Reference: https://oklch.net/"""

    result = helper.convert.oklch_to_srgb(lightness, chroma, hue)
    for result_value, expected_value in zip(result, expected):
        assert abs(result_value - expected_value) <= 1
