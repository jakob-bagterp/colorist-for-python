# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from colorist import BgColorHex, ColorHex

MOCK_DATASET = [
    ("#1AFFa1", does_not_raise()),
    ("1AFFa1", does_not_raise()),
    ("#1AF", does_not_raise()),
    ("1AF", does_not_raise()),
    ("#000000", does_not_raise()),
    ("000000", does_not_raise()),
    ("#000", does_not_raise()),
    ("000", does_not_raise()),
    ("#FfFFFF", does_not_raise()),
    ("FFfFFF", does_not_raise()),
    ("#ffF", does_not_raise()),
    ("Fff", does_not_raise()),
    ("#1AFFa10", pytest.raises(ValueError)),
    ("1AFFa10", pytest.raises(ValueError)),
    ("#1A", pytest.raises(ValueError)),
    ("1A", pytest.raises(ValueError)),
    ("#random", pytest.raises(ValueError)),
    ("random", pytest.raises(ValueError)),
]


@pytest.mark.parametrize("hex, expectation", MOCK_DATASET)
def test_exception_handling_of_color_hex(hex: str, expectation: Any) -> None:
    with expectation:
        _ = ColorHex(hex) is not None


@pytest.mark.parametrize("hex, expectation", MOCK_DATASET)
def test_exception_handling_of_background_color_hex(hex: str, expectation: Any) -> None:
    with expectation:
        _ = BgColorHex(hex) is not None
