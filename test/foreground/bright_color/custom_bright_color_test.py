# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import BrightColor

MIXED_PARAMETERS_MOCK_TEXT = "Both \033[92mgreen\033[0m and \033[93myellow\033[0m are nice colors\n"


@pytest.mark.parametrize("text, expected", [
    # F-strings and all color options:
    (f"Only color this {BrightColor.BLACK}word{BrightColor.OFF}.", "Only color this \033[90mword\033[0m.\n"),
    (f"Only color this {BrightColor.RED}word{BrightColor.OFF}.", "Only color this \033[91mword\033[0m.\n"),
    (f"Only color this {BrightColor.GREEN}word{BrightColor.OFF}.", "Only color this \033[92mword\033[0m.\n"),
    (f"Only color this {BrightColor.YELLOW}word{BrightColor.OFF}.", "Only color this \033[93mword\033[0m.\n"),
    (f"Only color this {BrightColor.BLUE}word{BrightColor.OFF}.", "Only color this \033[94mword\033[0m.\n"),
    (f"Only color this {BrightColor.MAGENTA}word{BrightColor.OFF}.", "Only color this \033[95mword\033[0m.\n"),
    (f"Only color this {BrightColor.CYAN}word{BrightColor.OFF}.", "Only color this \033[96mword\033[0m.\n"),
    (f"Only color this {BrightColor.WHITE}word{BrightColor.OFF}.", "Only color this \033[97mword\033[0m.\n"),
    (f"Only color this {BrightColor.DEFAULT}word{BrightColor.OFF}.", "Only color this \033[99mword\033[0m.\n"),

    # String concatenation:
    ("I want " + BrightColor.RED + "red" + BrightColor.OFF + " color inside this paragraph", "I want \033[91mred\033[0m color inside this paragraph\n"),

    # String format placeholders:
    ("Both {0}green{1} and {2}yellow{3} are nice colors".format(BrightColor.GREEN, BrightColor.OFF, BrightColor.YELLOW, BrightColor.OFF), MIXED_PARAMETERS_MOCK_TEXT),

    # Multiple and mixed parameters inside string:
    (f"Both {BrightColor.GREEN}green{BrightColor.OFF} and {BrightColor.YELLOW}yellow{BrightColor.OFF} are nice colors", MIXED_PARAMETERS_MOCK_TEXT),
])
def test_custom_text_bright_color(text: str, expected: str, capfd: object) -> None:
    print(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
