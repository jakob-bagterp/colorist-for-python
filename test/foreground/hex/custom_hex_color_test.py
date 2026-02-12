# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import ColorHex

BLACK_MOCK_TEXT = "Only color this \033[38;2;0;0;0mword\033[0m.\n"

WHITE_MOCK_TEXT = "Only color this \033[38;2;255;255;255mword\033[0m.\n"


@pytest.mark.parametrize(
    "hex, expected",
    [
        ("#000", BLACK_MOCK_TEXT),
        ("#000000", BLACK_MOCK_TEXT),
        ("000", BLACK_MOCK_TEXT),
        ("000000", BLACK_MOCK_TEXT),
        ("#fFf", WHITE_MOCK_TEXT),
        ("#fFFFFf", WHITE_MOCK_TEXT),
        ("fFf", WHITE_MOCK_TEXT),
        ("fFFFFf", WHITE_MOCK_TEXT),
        ("aB3", "Only color this \033[38;2;170;187;51mword\033[0m.\n"),
        ("#9b9Ac7", "Only color this \033[38;2;155;154;199mword\033[0m.\n"),
    ],
)
def test_custom_text_hex_color_f_string(hex: str, expected: str, capfd: object) -> None:
    color_hex = ColorHex(hex)
    print(f"Only color this {color_hex}word{ColorHex.OFF}.")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
