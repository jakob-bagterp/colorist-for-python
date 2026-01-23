# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import (BgBrightColor, BgColor, BgColorHex, BgColorHSL,
                      BgColorOKLCH, BgColorRGB, BgColorVGA, BrightColor, Color,
                      ColorHex, ColorHSL, ColorOKLCH, ColorRGB, ColorVGA,
                      Effect, style_text)


@pytest.mark.parametrize("text, styles, expected", [
    ("random text", [Color.YELLOW, Effect.BLINK], "\033[33m\033[5mrandom text\033[0m"),
])
def test_style_text_as_lambda_method(text: str,
                                     styles: list[Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | ColorOKLCH | BgColorOKLCH | Effect | str | None],
                                     expected: str,
                                     capfd: object) -> None:
    def styled_text(text: str):  # Equivalent to: lambda text: style_text(text, *styles)
        return style_text(text, *styles)

    output = styled_text(text)
    assert output == expected
    print(styled_text(text))
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"{expected}\n"
