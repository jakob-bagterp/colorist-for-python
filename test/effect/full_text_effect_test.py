# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal
from _config.callables import PrintEffectCallable, PrintEffectWithColorCallable

from colorist import (BgBrightColor, BgColor, BgColorHex, BgColorHSL, BgColorRGB, BrightColor, Color, ColorHex,
                      ColorHSL, ColorRGB, effect_blink, effect_bold, effect_dim, effect_hide, effect_reverse,
                      effect_underline)
from colorist.model.abc.color import BgColor_ABC, FgColor_ABC


@pytest.mark.parametrize("print_function, text, expected", [
    (effect_bold, "bold", "\033[1mbold\033[0m\n"),
    (effect_dim, "dimmed", "\033[2mdimmed\033[0m\n"),
    (effect_underline, "underline", "\033[4munderline\033[0m\n"),
    (effect_blink, "blink", "\033[5mblink\033[0m\n"),
    (effect_reverse, "reverse", "\033[7mreverse\033[0m\n"),
    (effect_hide, "hide", "\033[8mhide\033[0m\n"),
])
def test_full_text_with_effect(print_function: PrintEffectCallable, text: str, expected: str, capfd: object) -> None:
    print_function(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected


@pytest.mark.parametrize("print_function, text, color, expected", [
    (effect_blink, "cyan and blinking", Color.CYAN, "\033[36m\033[5mcyan and blinking\033[0m\n"),
    (effect_blink, "dusty pink and blinking", ColorRGB(194, 145, 164), "\033[38;2;194;145;164m\033[5mdusty pink and blinking\033[0m\n"),
    (effect_blink, "steel blue background and blinking", BgColorRGB(70, 130, 180), "\033[48;2;70;130;180m\033[5msteel blue background and blinking\033[0m\n"),
    (effect_underline, "bright red and underline", BrightColor.RED, "\033[91m\033[4mbright red and underline\033[0m\n"),
    (effect_underline, "mustard green and underline", ColorHSL(60, 56, 43), "\033[38;2;171;171;48m\033[4mmustard green and underline\033[0m\n"),
    (effect_underline, "only underline", None, "\033[4monly underline\033[0m\n"),
    (effect_underline, "only underline", "", "\033[4monly underline\033[0m\n"),
    (effect_bold, "red background and bold", BgColor.RED, "\033[41m\033[1mred background and bold\033[0m\n"),
    (effect_bold, "steel gray background and bold", BgColorHSL(190, 2, 49), "\033[48;2;122;126;127m\033[1msteel gray background and bold\033[0m\n"),
    (effect_dim, "bright blue background and dimmed", BgBrightColor.BLUE, "\033[104m\033[2mbright blue background and dimmed\033[0m\n"),
    (effect_dim, "watermelon red and dimmed", ColorHex("#ff5733"), "\033[38;2;255;87;51m\033[2mwatermelon red and dimmed\033[0m\n"),
    (effect_dim, "mint green background and dimmed", BgColorHex("#99ff99"), "\033[48;2;153;255;153m\033[2mmint green background and dimmed\033[0m\n"),
    (effect_reverse, "yellow background and reverse", BgColor.YELLOW, "\033[43m\033[7myellow background and reverse\033[0m\n"),
    (effect_hide, "green and hide", Color.GREEN, "\033[32m\033[8mgreen and hide\033[0m\n"),
])
def test_blink_full_text_effect_with_color(print_function: PrintEffectWithColorCallable, text: str, color: FgColor_ABC | BgColor_ABC, expected: str, capfd: object) -> None:
    print_function(text, color)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
