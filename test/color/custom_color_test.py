import terminal

from colorist import Color

RED_TEXT = "I want \033[31mred\033[0m color inside this paragraph\n"


def test_custom_text_color_1(capfd: object) -> None:
    print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == RED_TEXT


def test_custom_text_color_2(capfd: object) -> None:
    print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == "Both \033[32mgreen\033[0m and \033[33myellow\033[0m are nice colors\n"


def test_custom_text_color_1_string_concatenation(capfd: object) -> None:
    print("I want " + Color.RED + "red" + Color.OFF + " color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == RED_TEXT
