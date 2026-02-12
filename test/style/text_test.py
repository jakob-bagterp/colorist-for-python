# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest

from colorist import (
    BgBrightColor,
    BgColor,
    BgColorHex,
    BgColorHSL,
    BgColorOKLCH,
    BgColorRGB,
    BgColorVGA,
    BrightColor,
    Color,
    ColorHex,
    ColorHSL,
    ColorOKLCH,
    ColorRGB,
    ColorVGA,
    Effect,
    style_text,
)


@pytest.mark.parametrize(
    "text, styles, expected",
    [
        ("random text", [], "random text\033[0m"),
        ("random text", [None], "random text\033[0m"),
        ("random text", [Color.BLACK], "\033[30mrandom text\033[0m"),
        ("random text", [BrightColor.YELLOW], "\033[93mrandom text\033[0m"),
        ("random text", [ColorRGB(127, 57, 203)], "\033[38;2;127;57;203mrandom text\033[0m"),
        ("random text", [ColorHSL(360, 30, 70)], "\033[38;2;201;155;155mrandom text\033[0m"),
        ("random text", [ColorHex("#9b9Ac7")], "\033[38;2;155;154;199mrandom text\033[0m"),
        ("random text", [BgColor.BLUE], "\033[44mrandom text\033[0m"),
        ("random text", [BgBrightColor.MAGENTA], "\033[105mrandom text\033[0m"),
        ("random text", [BgColorRGB(255, 144, 168)], "\033[48;2;255;144;168mrandom text\033[0m"),
        ("random text", [BgColorHSL(250, 50, 55)], "\033[48;2;101;82;197mrandom text\033[0m"),
        ("random text", [BgColorHex("aB3")], "\033[48;2;170;187;51mrandom text\033[0m"),
        ("random text", [Effect.BOLD], "\033[1mrandom text\033[0m"),
        (
            "random text",
            [ColorRGB(57, 33, 253), BgColor.CYAN, Effect.BLINK],
            "\033[38;2;57;33;253m\033[46m\033[5mrandom text\033[0m",
        ),
        ("random text", [ColorVGA(57), BgColor.CYAN, Effect.BLINK], "\033[38;5;57m\033[46m\033[5mrandom text\033[0m"),
        ("random text", [BgColorVGA(251)], "\033[48;5;251mrandom text\033[0m"),
        ("random text", ["\033[48;5;251m"], "\033[48;5;251mrandom text\033[0m"),
        ("random text", [ColorOKLCH(0.7, 0.3, 332)], "\033[38;2;254;37;238mrandom text\033[0m"),
        ("random text", [BgColorOKLCH(0.54, 0.15, 141)], "\033[48;2;51;130;37mrandom text\033[0m"),
    ],
)
def test_style_text(
    text: str,
    styles: list[
        Color
        | BrightColor
        | ColorVGA
        | ColorRGB
        | ColorHSL
        | ColorHex
        | BgColor
        | BgBrightColor
        | BgColorVGA
        | BgColorRGB
        | BgColorHSL
        | BgColorHex
        | ColorOKLCH
        | BgColorOKLCH
        | Effect
        | str
        | None
    ],
    expected: str,
) -> None:
    output = style_text(text, *styles)
    assert output == expected
