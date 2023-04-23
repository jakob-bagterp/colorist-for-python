# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import (BgBrightColor, BgColor, BgColorHex, BgColorHSL,
                      BgColorRGB, BrightColor, Color, ColorHex, ColorHSL,
                      ColorRGB, Effect, print_color)


@pytest.mark.parametrize("text, color, bg_color, effect, expected", [
    ("random text", None, None, None, "random text\033[0m\n"),
    ("random text", Color.BLACK, None, None, "\033[30mrandom text\033[0m\n"),
    ("random text", BrightColor.YELLOW, None, None, "\033[93mrandom text\033[0m\n"),
    ("random text", ColorRGB(127, 57, 203), None, None, "\033[38;2;127;57;203mrandom text\033[0m\n"),
    ("random text", ColorHSL(360, 30, 70), None, None, "\033[38;2;201;155;155mrandom text\033[0m\n"),
    ("random text", ColorHex("#9b9Ac7"), None, None, "\033[38;2;155;154;199mrandom text\033[0m\n"),
    ("random text", None, BgColor.BLUE, None, "\033[44mrandom text\033[0m\n"),
    ("random text", None, BgBrightColor.MAGENTA, None, "\033[105mrandom text\033[0m\n"),
    ("random text", None, BgColorRGB(255, 144, 168), None, "\033[48;2;255;144;168mrandom text\033[0m\n"),
    ("random text", None, BgColorHSL(250, 50, 55), None, "\033[48;2;101;82;197mrandom text\033[0m\n"),
    ("random text", None, BgColorHex("aB3"), None, "\033[48;2;170;187;51mrandom text\033[0m\n"),
])
def test_full_text_general_print_color(text: str,
                                       color: Color | BrightColor | ColorRGB | ColorHSL | ColorHex | None,
                                       bg_color: BgColor | BgBrightColor | BgColorRGB | BgColorHSL | BgColorHex | None,
                                       effect: Effect | None,
                                       expected: str,
                                       capfd: object
                                       ) -> None:
    print_color(text, color, bg_color, effect)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
