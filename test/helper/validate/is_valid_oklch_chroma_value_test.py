# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "input, expected",
    [
        (0, True),
        (0.4, True),
        (0.3, True),
        (0.0, True),
        (0.1, True),
        (0.2, True),
        (0.41, False),
        (0.5, False),
        (-0.1, False),
        (-1, False),
    ],
)
def test_is_valid_oklch_chroma_value(input: float, expected: bool) -> None:
    assert helper.validate.is_valid_oklch_chroma_value(input) is expected
