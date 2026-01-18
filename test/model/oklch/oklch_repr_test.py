# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import BgColorOKLCH, ColorOKLCH

MOCK_DATASET: list[tuple[tuple[float, float, float], str]] = [
    ((0, 0, 0), "L: 0, C: 0, H: 0"),
    ((0.5, 0.2, 0.0), "L: 0.5, C: 0.2, H: 0.0"),
    ((0.7, 0.1, 45.0), "L: 0.7, C: 0.1, H: 45.0"),
    ((0.7, 0.1, 45), "L: 0.7, C: 0.1, H: 45"),
]


@pytest.mark.parametrize("oklch, expected_repr", MOCK_DATASET)
def test_repr_of_color_oklch(oklch: tuple[float, float, float], expected_repr: str) -> None:
    color_oklch = ColorOKLCH(*oklch)
    assert repr(color_oklch) == expected_repr


@pytest.mark.parametrize("oklch, expected_repr", MOCK_DATASET)
def test_repr_of_background_color_oklch(oklch: tuple[float, float, float], expected_repr: str) -> None:
    color_oklch = BgColorOKLCH(*oklch)
    assert repr(color_oklch) == expected_repr
