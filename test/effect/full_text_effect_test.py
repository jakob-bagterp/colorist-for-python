# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal
from _config.callables import PrintEffectCallable, PrintEffectWithColorCallable

from colorist import (BrightColor, Color, effect_blink, effect_bold,
                      effect_dim, effect_hide, effect_reverse,
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
    (effect_underline, "bright red and underline", BrightColor.RED, "\033[91m\033[4mbright red and underline\033[0m\n"),
    (effect_underline, "only underline", None, "\033[4monly underline\033[0m\n"),
    (effect_underline, "only underline", "", "\033[4monly underline\033[0m\n"),
])
def test_blink_full_text_effect_with_color(print_function: PrintEffectWithColorCallable, text: str, color: FgColor_ABC | BgColor_ABC, expected: str, capfd: object) -> None:
    print_function(text, color)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
