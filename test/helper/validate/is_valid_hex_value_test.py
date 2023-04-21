# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import helper


@pytest.mark.parametrize("input, expected", [
    ("#1AFFa1", True),
    ("1AFFa1", True),
    ("#1AF", True),
    ("1AF", True),
    ("#000000", True),
    ("000000", True),
    ("#000", True),
    ("000", True),
    ("#FfFFFF", True),
    ("FFfFFF", True),
    ("#ffF", True),
    ("Fff", True),
    ("#1AFFa10", False),
    ("1AFFa10", False),
    ("#1A", False),
    ("1A", False),
    ("#random", False),
    ("random", False),
])
def test_is_valid_hex_value(input: str, expected: bool) -> None:
    assert helper.validate.is_valid_hex_value(input) is expected
