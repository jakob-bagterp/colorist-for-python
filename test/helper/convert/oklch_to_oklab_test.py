# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "lightness, chroma, hue, expected",
    [
        (0.0, 0.0, 0.0, (0.0, 0.0, 0.0)),  # Neutral black (chroma 0) should map to neutral black in Oklab.
        (1.0, 0.0, 180.0, (1.0, 0.0, 0.0)),  # Neutral white (chroma 0) should map to neutral white in Oklab.
        (0.5, 0.2, 0.0, (0.5, 0.2, 0.0)),  # Pure red-ish (hue 0° should map to positive a).
        (0.5, 0.2, 90.0, (0.5, 0.0, 0.2)),  # Pure yellow/green-ish (hue 90° should map to positive b).
        (0.5, 0.2, 180.0, (0.5, -0.2, 0.0)),  # Pure green-ish (hue 180° should map to negative a).
        (0.5, 0.2, 270.0, (0.5, 0.0, -0.2)),  # Pure blue-ish (hue 270° should map to negative b).
        (0.7, 0.1, 45.0, (0.7, 0.070710678, 0.070710678)),  # A specific diagonal (hue 45°).
    ],
)
def test_convert_oklch_to_oklab(
    lightness: float, chroma: float, hue: float, expected: tuple[float, float, float]
) -> None:
    assert helper.convert.oklch_to_oklab(lightness, chroma, hue) == pytest.approx(expected, abs=1e-9)
