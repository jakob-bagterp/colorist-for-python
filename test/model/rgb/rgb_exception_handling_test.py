from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from colorist import BgColorRGB, ColorRGB

MOCK_DATASET = [
    ((0, 0, 0), does_not_raise()),
    ((137, 53, 238), does_not_raise()),
    ((255, 255, 255), does_not_raise()),
    ((0.0, 0.0, 0.0), does_not_raise()),
    ((255.0, 255.0, 255.0), does_not_raise()),
    ((255.1, 255.0, 255.0), pytest.raises(ValueError)),
    ((255.0, 255.1, 255.0), pytest.raises(ValueError)),
    ((255.0, 255.0, 255.1), pytest.raises(ValueError)),
    ((-1, 0, 0), pytest.raises(ValueError)),
    ((0, -1, 0), pytest.raises(ValueError)),
    ((0, 0, -1), pytest.raises(ValueError)),
]


@pytest.mark.parametrize("rgb, expectation", MOCK_DATASET)
def test_exception_handling_of_color_rgb(rgb: tuple[int, int, int], expectation: Any) -> None:
    with expectation:
        _ = ColorRGB(*rgb) is not None


@pytest.mark.parametrize("rgb, expectation", MOCK_DATASET)
def test_exception_handling_of_background_color_rgb(rgb: tuple[int, int, int], expectation: Any) -> None:
    with expectation:
        _ = BgColorRGB(*rgb) is not None
