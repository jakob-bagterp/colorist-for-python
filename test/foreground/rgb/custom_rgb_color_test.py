# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import ColorRGB


@pytest.mark.parametrize("rgb, expected", [
    ((255, 255, 255), "Only color this \033[38;2;255;255;255mword\033[0m.\n"),
    ((0, 0, 0), "Only color this \033[38;2;0;0;0mword\033[0m.\n"),
    ((127, 57, 203), "Only color this \033[38;2;127;57;203mword\033[0m.\n"),
])
def test_custom_text_rgb_color_f_string(rgb: tuple[int, int, int], expected: str, capfd: object) -> None:
    color_rgb = ColorRGB(*rgb)
    print(f"Only color this {color_rgb}word{ColorRGB.OFF}.")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
