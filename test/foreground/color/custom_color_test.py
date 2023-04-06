import pytest
import terminal

from colorist import Color


@pytest.mark.parametrize("text, expected", [
    # F-strings and all color options:
    (f"Only color this {Color.BLACK}word{Color.OFF}.", "Only color this \033[30mword\033[0m.\n"),
    (f"Only color this {Color.RED}word{Color.OFF}.", "Only color this \033[31mword\033[0m.\n"),
    (f"Only color this {Color.GREEN}word{Color.OFF}.", "Only color this \033[32mword\033[0m.\n"),
    (f"Only color this {Color.YELLOW}word{Color.OFF}.", "Only color this \033[33mword\033[0m.\n"),
    (f"Only color this {Color.BLUE}word{Color.OFF}.", "Only color this \033[34mword\033[0m.\n"),
    (f"Only color this {Color.MAGENTA}word{Color.OFF}.", "Only color this \033[35mword\033[0m.\n"),
    (f"Only color this {Color.CYAN}word{Color.OFF}.", "Only color this \033[36mword\033[0m.\n"),
    (f"Only color this {Color.WHITE}word{Color.OFF}.", "Only color this \033[37mword\033[0m.\n"),
    (f"Only color this {Color.DEFAULT}word{Color.OFF}.", "Only color this \033[39mword\033[0m.\n"),

    # String concatenation:
    ("I want " + Color.RED + "red" + Color.OFF + " color inside this paragraph", "I want \033[31mred\033[0m color inside this paragraph\n"),

    # Multiple and mixed parameters inside string:
    (f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors", "Both \033[32mgreen\033[0m and \033[33myellow\033[0m are nice colors\n"),
])
def test_custom_text_color(text: str, expected: str, capfd: object) -> None:
    print(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
