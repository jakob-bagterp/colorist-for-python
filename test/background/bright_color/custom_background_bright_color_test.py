import terminal

from colorist import BgBrightColor

CYAN_BG_TEXT = "I want \033[106mcyan\033[0m background color inside this paragraph\n"


def test_custom_text_background_color_1(capfd: object) -> None:
    print(f"I want {BgBrightColor.CYAN}cyan{BgBrightColor.OFF} background color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == CYAN_BG_TEXT


def test_custom_text_background_color_1_string_concatenation(capfd: object) -> None:
    print("I want " + BgBrightColor.CYAN + "cyan" + BgBrightColor.OFF + " background color inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == CYAN_BG_TEXT
