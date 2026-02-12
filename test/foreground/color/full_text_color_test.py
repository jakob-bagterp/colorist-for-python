# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal
from _config.callables import PrintFullTextCallable

from colorist import black, blue, cyan, green, magenta, red, white, yellow


@pytest.mark.parametrize(
    "print_function, text, expected",
    [
        (black, "black", "\033[30mblack\033[0m\n"),
        (red, "red", "\033[31mred\033[0m\n"),
        (green, "green", "\033[32mgreen\033[0m\n"),
        (yellow, "yellow", "\033[33myellow\033[0m\n"),
        (blue, "blue", "\033[34mblue\033[0m\n"),
        (magenta, "magenta", "\033[35mmagenta\033[0m\n"),
        (cyan, "cyan", "\033[36mcyan\033[0m\n"),
        (white, "white", "\033[37mwhite\033[0m\n"),
    ],
)
def test_full_text_color(print_function: PrintFullTextCallable, text: str, expected: str, capfd: object) -> None:
    print_function(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
