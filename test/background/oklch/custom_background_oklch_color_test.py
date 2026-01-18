# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import BgColorOKLCH


@pytest.mark.parametrize("oklch, expected", [
    ((0, 0, 0), "Only color this \033[48;2;0;0;0mword\033[0m.\n"),
    ((1, 0, 0), "Only color this \033[48;2;255;255;255mword\033[0m.\n"),
    ((0.5, 0.2, 0.0), "Only color this \033[48;2;179;5;94mword\033[0m.\n"),
    ((0.7, 0.1, 45.0), "Only color this \033[48;2;210;138;105mword\033[0m.\n"),
    ((0.7, 0.1, 45), "Only color this \033[48;2;210;138;105mword\033[0m.\n"),
])
def test_custom_text_background_oklch_color_f_string(oklch: tuple[float, float, float], expected: str, capfd: object) -> None:
    bg_color_oklch = BgColorOKLCH(*oklch)
    print(f"Only color this {bg_color_oklch}word{BgColorOKLCH.OFF}.")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
