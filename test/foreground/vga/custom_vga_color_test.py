# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import ColorVGA


@pytest.mark.parametrize(
    "vga, expected",
    [
        (255, "Only color this \033[38;5;255mword\033[0m.\n"),
        (0, "Only color this \033[38;5;0mword\033[0m.\n"),
        (127, "Only color this \033[38;5;127mword\033[0m.\n"),
    ],
)
def test_custom_text_vga_color_f_string(vga: int, expected: str, capfd: object) -> None:
    color_vga = ColorVGA(vga)
    print(f"Only color this {color_vga}word{ColorVGA.OFF}.")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
