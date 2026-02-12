# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal
from _config.callables import PrintFullTextCallable

from colorist import bg_black, bg_blue, bg_cyan, bg_green, bg_magenta, bg_red, bg_white, bg_yellow


@pytest.mark.parametrize(
    "print_function, text, expected",
    [
        (bg_black, "black", "\033[40mblack\033[0m\n"),
        (bg_red, "red", "\033[41mred\033[0m\n"),
        (bg_green, "green", "\033[42mgreen\033[0m\n"),
        (bg_yellow, "yellow", "\033[43myellow\033[0m\n"),
        (bg_blue, "blue", "\033[44mblue\033[0m\n"),
        (bg_magenta, "magenta", "\033[45mmagenta\033[0m\n"),
        (bg_cyan, "cyan", "\033[46mcyan\033[0m\n"),
        (bg_white, "white", "\033[47mwhite\033[0m\n"),
    ],
)
def test_full_text_background_color(
    print_function: PrintFullTextCallable, text: str, expected: str, capfd: object
) -> None:
    print_function(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
