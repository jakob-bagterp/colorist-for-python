# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import BgBrightColor

MIXED_PARAMETERS_MOCK_TEXT = "Both \033[102mgreen\033[0m and \033[103myellow\033[0m are nice colors\n"


@pytest.mark.parametrize("text, expected", [
    # F-strings and all color options:
    (f"Only color this {BgBrightColor.BLACK}word{BgBrightColor.OFF}.", "Only color this \033[100mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.RED}word{BgBrightColor.OFF}.", "Only color this \033[101mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.GREEN}word{BgBrightColor.OFF}.", "Only color this \033[102mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.YELLOW}word{BgBrightColor.OFF}.", "Only color this \033[103mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.BLUE}word{BgBrightColor.OFF}.", "Only color this \033[104mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.MAGENTA}word{BgBrightColor.OFF}.", "Only color this \033[105mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.CYAN}word{BgBrightColor.OFF}.", "Only color this \033[106mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.WHITE}word{BgBrightColor.OFF}.", "Only color this \033[107mword\033[0m.\n"),
    (f"Only color this {BgBrightColor.DEFAULT}word{BgBrightColor.OFF}.", "Only color this \033[109mword\033[0m.\n"),

    # String concatenation:
    ("I want " + BgBrightColor.RED + "red" + BgBrightColor.OFF + " color inside this paragraph", "I want \033[101mred\033[0m color inside this paragraph\n"),

    # String format placeholders:
    ("Both {0}green{1} and {2}yellow{3} are nice colors".format(BgBrightColor.GREEN, BgBrightColor.OFF, BgBrightColor.YELLOW, BgBrightColor.OFF), MIXED_PARAMETERS_MOCK_TEXT),

    # Multiple and mixed parameters inside string:
    (f"Both {BgBrightColor.GREEN}green{BgBrightColor.OFF} and {BgBrightColor.YELLOW}yellow{BgBrightColor.OFF} are nice colors", MIXED_PARAMETERS_MOCK_TEXT),
])
def test_custom_text_background_bright_color(text: str, expected: str, capfd: object) -> None:
    print(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
