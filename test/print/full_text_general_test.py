# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import (BgBrightColor, BgColor, BgColorHex, BgColorHSL,
                      BgColorRGB, BrightColor, Color, ColorHex, ColorHSL,
                      ColorRGB, Effect, print_color)


@pytest.mark.parametrize("text, color, bg_color, effect, expected", [
    ("random text", Color.BLACK, None, None, "\033[30mrandom text\033[0m\n"),
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
