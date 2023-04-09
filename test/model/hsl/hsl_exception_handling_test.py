from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from colorist import BgColorHSL, ColorHSL

MOCK_DATASET = [
    ((0, 0, 0), does_not_raise()),
    ((137, 24, 82), does_not_raise()),
    ((360, 100, 100), does_not_raise()),
    ((0.0, 0.0, 0.0), does_not_raise()),
    ((360.0, 100.0, 100.0), does_not_raise()),
    ((360.1, 100.0, 100.0), pytest.raises(ValueError)),
    ((360.0, 100.1, 100.0), pytest.raises(ValueError)),
    ((360.0, 100.0, 100.1), pytest.raises(ValueError)),
    ((-1, 0, 0), pytest.raises(ValueError)),
    ((0, -1, 0), pytest.raises(ValueError)),
    ((0, 0, -1), pytest.raises(ValueError)),
]


@pytest.mark.parametrize("hsl, expectation", MOCK_DATASET)
def test_exception_handling_of_color_hsl(hsl: tuple[float, float, float], expectation: Any) -> None:
    with expectation:
        _ = ColorHSL(*hsl) is not None


@pytest.mark.parametrize("hsl, expectation", MOCK_DATASET)
def test_exception_handling_of_background_color_hsl(hsl: tuple[float, float, float], expectation: Any) -> None:
    with expectation:
        _ = BgColorHSL(*hsl) is not None
