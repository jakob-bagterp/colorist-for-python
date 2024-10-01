# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from colorist import BgColorVGA, ColorVGA

MOCK_DATASET = [
    (0, does_not_raise()),
    (137, does_not_raise()),
    (255, does_not_raise()),
    (0.0, does_not_raise()),
    (255.0, does_not_raise()),
    (255.1, pytest.raises(ValueError)),
    (-1, pytest.raises(ValueError)),
]


@pytest.mark.parametrize("vga, expectation", MOCK_DATASET)
def test_exception_handling_of_color_vga(vga: int, expectation: Any) -> None:
    with expectation:
        _ = ColorVGA(vga) is not None


@pytest.mark.parametrize("vga, expectation", MOCK_DATASET)
def test_exception_handling_of_background_color_vga(vga: int, expectation: Any) -> None:
    with expectation:
        _ = BgColorVGA(vga) is not None
