# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import vga


@pytest.mark.parametrize("text, vga_color", [
    ("random text", 0),
    ("random text", 255),
    ("random text", 135),
])
def test_full_text_vga_color(text: str, vga_color: int, capfd: object) -> None:
    vga(text, vga_color)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[38;5;{vga_color}m{text}\033[0m\n"
