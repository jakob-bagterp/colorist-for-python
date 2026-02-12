# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize(
    "input, expected",
    [(0, True), (117, True), (255, True), (0.0, True), (255.0, True), (255.1, False), (256, False), (-1, False)],
)
def test_is_valid_rgb_value(input: int, expected: bool) -> None:
    assert helper.validate.is_valid_rgb_value(input) is expected
