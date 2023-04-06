import pytest
import terminal

from colorist import BgColor


@pytest.mark.parametrize("text, expected", [
    # F-strings and all color options:
    (f"Only color this {BgColor.BLACK}word{BgColor.OFF}.", "Only color this \033[40mword\033[0m.\n"),
    (f"Only color this {BgColor.RED}word{BgColor.OFF}.", "Only color this \033[41mword\033[0m.\n"),
    (f"Only color this {BgColor.GREEN}word{BgColor.OFF}.", "Only color this \033[42mword\033[0m.\n"),
    (f"Only color this {BgColor.YELLOW}word{BgColor.OFF}.", "Only color this \033[43mword\033[0m.\n"),
    (f"Only color this {BgColor.BLUE}word{BgColor.OFF}.", "Only color this \033[44mword\033[0m.\n"),
    (f"Only color this {BgColor.MAGENTA}word{BgColor.OFF}.", "Only color this \033[45mword\033[0m.\n"),
    (f"Only color this {BgColor.CYAN}word{BgColor.OFF}.", "Only color this \033[46mword\033[0m.\n"),
    (f"Only color this {BgColor.WHITE}word{BgColor.OFF}.", "Only color this \033[47mword\033[0m.\n"),
    (f"Only color this {BgColor.DEFAULT}word{BgColor.OFF}.", "Only color this \033[49mword\033[0m.\n"),

    # String concatenation:
    ("I want " + BgColor.RED + "red" + BgColor.OFF + " color inside this paragraph", "I want \033[41mred\033[0m color inside this paragraph\n"),

    # Multiple and mixed parameters inside string:
    (f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice colors", "Both \033[42mgreen\033[0m and \033[43myellow\033[0m are nice colors\n"),
])
def test_custom_text_background_color(text: str, expected: str, capfd: object) -> None:
    print(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
