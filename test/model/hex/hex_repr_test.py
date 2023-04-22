# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import BgColorHex, ColorHex

MOCK_DATASET = [
    ("#000", "Hex: #000"),
    ("#000000", "Hex: #000000"),
    ("000", "Hex: #000"),
    ("000000", "Hex: #000000"),
    ("#fFf", "Hex: #fff"),
    ("#fFFFFf", "Hex: #ffffff"),
    ("fFf", "Hex: #fff"),
    ("fFFFFf", "Hex: #ffffff"),
    ("aB3", "Hex: #ab3"),
    ("#9b9Ac7", "Hex: #9b9ac7"),
]


@pytest.mark.parametrize("hex, expected_repr", MOCK_DATASET)
def test_repr_of_color_hex(hex: str, expected_repr: str) -> None:
    color_hex = ColorHex(hex)
    assert repr(color_hex) == expected_repr


@pytest.mark.parametrize("hex, expected_repr", MOCK_DATASET)
def test_repr_of_background_color_hex(hex: str, expected_repr: str) -> None:
    color_hex = BgColorHex(hex)
    assert repr(color_hex) == expected_repr
