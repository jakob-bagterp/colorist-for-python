# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from colorist import BgColorOKLCH, ColorOKLCH

MOCK_DATASET: list[tuple[tuple[float, float, float], Any]] = [
    ((0, 0, 0), does_not_raise()),
    ((0.0, 0.0, 0.0), does_not_raise()),
    ((0.5, 0.2, 180), does_not_raise()),
    ((1, 0.4, 360), does_not_raise()),
    ((1.1, 0.4, 360), pytest.raises(ValueError)),
    ((1, 0.41, 360), pytest.raises(ValueError)),
    ((1, 0.4, 361), pytest.raises(ValueError)),
    ((-1, 0, 0), pytest.raises(ValueError)),
    ((0, -1, 0), pytest.raises(ValueError)),
    ((0, 0, -1), pytest.raises(ValueError)),
]


@pytest.mark.parametrize("oklch, expectation", MOCK_DATASET)
def test_exception_handling_of_color_oklch(oklch: tuple[float, float, float], expectation: Any) -> None:
    with expectation:
        _ = ColorOKLCH(*oklch) is not None


@pytest.mark.parametrize("oklch, expectation", MOCK_DATASET)
def test_exception_handling_of_background_color_oklch(oklch: tuple[float, float, float], expectation: Any) -> None:
    with expectation:
        _ = BgColorOKLCH(*oklch) is not None
