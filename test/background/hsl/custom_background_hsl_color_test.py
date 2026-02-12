# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import BgColorHSL


@pytest.mark.parametrize(
    "hsl, expected",
    [
        ((100, 20, 80), "Only color this \033[48;2;200;214;193mword\033[0m.\n"),
        ((250, 50, 55), "Only color this \033[48;2;101;82;197mword\033[0m.\n"),
        ((360, 30, 70), "Only color this \033[48;2;201;155;155mword\033[0m.\n"),
        ((0, 100, 0), "Only color this \033[48;2;0;0;0mword\033[0m.\n"),
        ((0, 0, 0), "Only color this \033[48;2;0;0;0mword\033[0m.\n"),
    ],
)
def test_custom_text_background_hsl_color_f_string(
    hsl: tuple[float, float, float], expected: str, capfd: object
) -> None:
    bg_color_hsl = BgColorHSL(*hsl)
    print(f"Only color this {bg_color_hsl}word{BgColorHSL.OFF}.")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
