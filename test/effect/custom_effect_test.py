import terminal

from colorist import Color, Effect


def test_custom_text_effect_1(capfd: object) -> None:
    print(f"I want {Effect.UNDERLINE}underlined text{Effect.UNDERLINE_OFF} inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == "I want \033[4munderlined text\033[24m inside this paragraph\n"


def test_custom_text_effect_2(capfd: object) -> None:
    print(f"I want {Effect.BOLD}emphasized text{Effect.BOLD_OFF} inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == "I want \033[1memphasized text\033[21m inside this paragraph\n"


def test_custom_text_effect_3(capfd: object) -> None:
    print(f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph")
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == "I want both \033[31mcolored and \033[5mblinking\033[25m text\033[0m inside this paragraph\n"
