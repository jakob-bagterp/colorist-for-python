import terminal

from colorist import BrightColor

CYAN_TEXT = "I want \033[96mcyan\033[0m color inside this paragraph\n"


def test_custom_text_color_1(capfd: object) -> None:
    print(f"I want {BrightColor.CYAN}cyan{BrightColor.OFF} color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == CYAN_TEXT


def test_custom_text_color_1_string_concatenation(capfd: object) -> None:
    print("I want " + BrightColor.CYAN + "cyan" + BrightColor.OFF + " color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == CYAN_TEXT
