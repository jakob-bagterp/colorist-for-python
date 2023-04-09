# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal
from _config.callables import PrintFullTextCallable

from colorist import (bright_black, bright_blue, bright_cyan, bright_green,
                      bright_magenta, bright_red, bright_white, bright_yellow)


@pytest.mark.parametrize("print_function, text, expected", [
    (bright_black, "black", "\033[90mblack\033[0m\n"),
    (bright_red, "red", "\033[91mred\033[0m\n"),
    (bright_green, "green", "\033[92mgreen\033[0m\n"),
    (bright_yellow, "yellow", "\033[93myellow\033[0m\n"),
    (bright_blue, "blue", "\033[94mblue\033[0m\n"),
    (bright_magenta, "magenta", "\033[95mmagenta\033[0m\n"),
    (bright_cyan, "cyan", "\033[96mcyan\033[0m\n"),
    (bright_white, "white", "\033[97mwhite\033[0m\n"),
])
def test_full_text_bright_color(print_function: PrintFullTextCallable, text: str, expected: str, capfd: object) -> None:
    print_function(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
