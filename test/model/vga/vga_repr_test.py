# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import BgColorVGA, ColorVGA

MOCK_DATASET = [
    (0, "VGA: 0"),
    (137, "VGA: 137"),
    (255, "VGA: 255"),
]


@pytest.mark.parametrize("vga, expected_repr", MOCK_DATASET)
def test_repr_of_color_vga(vga: int, expected_repr: str) -> None:
    color_vga = ColorVGA(vga)
    assert repr(color_vga) == expected_repr


@pytest.mark.parametrize("vga, expected_repr", MOCK_DATASET)
def test_repr_of_background_color_vga(vga: int, expected_repr: str) -> None:
    color_vga = BgColorVGA(vga)
    assert repr(color_vga) == expected_repr
