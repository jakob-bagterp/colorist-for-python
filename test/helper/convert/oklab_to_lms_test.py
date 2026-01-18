# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("lightness, a, b, expected", [
    (0.0, 0.0, 0.0, (0.0, 0.0, 0.0)),  # Pure black should map to zero in LMS values.
    (1.0, 0.0, 0.0, (1.0, 1.0, 1.0)),  # Reference white should map to (1, 1, 1), which is a key design constraint of the Oklab specification.
    (0.5, 0.0, 0.0, (0.125, 0.125, 0.125)),  # Mid-grey lightness should map to (0.125, 0.125, 0.125) in LMS.
    (0.627955, 0.224863, 0.125846, (0.41222072025249173, 0.21190313436020206, 0.08830245941565427)),  # Standard red (approximate sRGB red in Oklab), which are values from the Oklab specification.
    (0.5, -0.1, -0.1, (0.08448076377737333, 0.1381411082458256, 0.2598125062834733)),  # Negative coordinates (chroma tests) that verifies the linear matrix coefficients for a and b channels.
])
def test_convert_oklab_to_lms(lightness: float, a: float, b: float, expected: tuple[float, float, float]) -> None:
    assert helper.convert.oklab_to_lms(lightness, a, b) == pytest.approx(expected, rel=1e-5)
