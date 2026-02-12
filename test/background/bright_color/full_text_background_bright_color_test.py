# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal
from _config.callables import PrintFullTextCallable

from colorist import (
    bg_bright_black,
    bg_bright_blue,
    bg_bright_cyan,
    bg_bright_green,
    bg_bright_magenta,
    bg_bright_red,
    bg_bright_white,
    bg_bright_yellow,
)


@pytest.mark.parametrize(
    "print_function, text, expected",
    [
        (bg_bright_black, "black", "\033[100mblack\033[0m\n"),
        (bg_bright_red, "red", "\033[101mred\033[0m\n"),
        (bg_bright_green, "green", "\033[102mgreen\033[0m\n"),
        (bg_bright_yellow, "yellow", "\033[103myellow\033[0m\n"),
        (bg_bright_blue, "blue", "\033[104mblue\033[0m\n"),
        (bg_bright_magenta, "magenta", "\033[105mmagenta\033[0m\n"),
        (bg_bright_cyan, "cyan", "\033[106mcyan\033[0m\n"),
        (bg_bright_white, "white", "\033[107mwhite\033[0m\n"),
    ],
)
def test_full_text_bright_background_color(
    print_function: PrintFullTextCallable, text: str, expected: str, capfd: object
) -> None:
    print_function(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
