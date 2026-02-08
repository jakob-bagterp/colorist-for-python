# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import (BgBrightColor, BgColor, BgColorHex, BgColorHSL, BgColorOKLCH, BgColorRGB, BgColorVGA, BrightColor,
                      Color, ColorHex, ColorHSL, ColorOKLCH, ColorRGB, ColorVGA, Effect, print_color)


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
    ("random text", None, None, Effect.BOLD, "\033[1mrandom text\033[0m\n"),
    ("random text", ColorRGB(57, 33, 253), BgColor.CYAN, Effect.BLINK, "\033[38;2;57;33;253m\033[46m\033[5mrandom text\033[0m\n"),
    ("random text", ColorVGA(57), BgColor.CYAN, Effect.BLINK, "\033[38;5;57m\033[46m\033[5mrandom text\033[0m\n"),
    ("random text", None, BgColorVGA(251), None, "\033[48;5;251mrandom text\033[0m\n"),
    ("random text", ColorOKLCH(0.7, 0.3, 332), None, None, "\033[38;2;254;37;238mrandom text\033[0m\n"),
    ("random text", None, BgColorOKLCH(0.54, 0.15, 141), None, "\033[48;2;51;130;37mrandom text\033[0m\n"),
])
def test_full_text_general_print_color(text: str,
                                       color: Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | ColorOKLCH | None,
                                       bg_color: BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | BgColorOKLCH | None,
                                       effect: Effect | None,
                                       expected: str,
                                       capfd: object
                                       ) -> None:
    print_color(text, color, bg_color, effect)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
