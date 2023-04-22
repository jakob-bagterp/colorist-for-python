# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import BgColorRGB, ColorRGB

MOCK_DATASET = [
    ((0, 0, 0), "R: 0, G: 0, B: 0"),
    ((137, 53, 238), "R: 137, G: 53, B: 238"),
    ((255, 255, 255), "R: 255, G: 255, B: 255"),
]


@pytest.mark.parametrize("rgb, expected_repr", MOCK_DATASET)
def test_repr_of_color_rgb(rgb: tuple[int, int, int], expected_repr: str) -> None:
    color_rgb = ColorRGB(*rgb)
    assert repr(color_rgb) == expected_repr


@pytest.mark.parametrize("rgb, expected_repr", MOCK_DATASET)
def test_repr_of_background_color_rgb(rgb: tuple[int, int, int], expected_repr: str) -> None:
    color_rgb = BgColorRGB(*rgb)
    assert repr(color_rgb) == expected_repr
