# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import hex


@pytest.mark.parametrize("text, hex_input, rgb_expected", [
    ("random text", "#000", (0, 0, 0)),
    ("random text", "#000000", (0, 0, 0)),
    ("random text", "000", (0, 0, 0)),
    ("random text", "000000", (0, 0, 0)),
    ("random text", "#fFf", (255, 255, 255)),
    ("random text", "#fFFFFf", (255, 255, 255)),
    ("random text", "fFf", (255, 255, 255)),
    ("random text", "fFFFFf", (255, 255, 255)),
    ("random text", "aB3", (170, 187, 51)),
    ("random text", "#9b9Ac7", (155, 154, 199)),
])
def test_full_text_hex_color(text: str, hex_input: str, rgb_expected: tuple[int, int, int], capfd: object) -> None:
    hex(text, hex_input)
    terminal_output = terminal.get_output(capfd)
    red, green, blue = rgb_expected
    assert terminal_output == f"\033[38;2;{red};{green};{blue}m{text}\033[0m\n"
