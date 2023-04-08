import pytest
import terminal

from colorist import Color, Effect

MIXED_PARAMETERS_MOCK_TEXT = "I want both \033[31mcolored and \033[5mblinking\033[25m text\033[0m inside this paragraph\n"


@pytest.mark.parametrize("text, expected", [
    # F-strings and all effect options:
    (f"Only effect for this {Effect.BOLD}word{Effect.BOLD_OFF}.", "Only effect for this \033[1mword\033[21m.\n"),
    (f"Only effect for this {Effect.DIM}word{Effect.DIM_OFF}.", "Only effect for this \033[2mword\033[22m.\n"),
    (f"Only effect for this {Effect.UNDERLINE}word{Effect.UNDERLINE_OFF}.", "Only effect for this \033[4mword\033[24m.\n"),
    (f"Only effect for this {Effect.BLINK}word{Effect.BLINK_OFF}.", "Only effect for this \033[5mword\033[25m.\n"),
    (f"Only effect for this {Effect.REVERSE}word{Effect.REVERSE_OFF}.", "Only effect for this \033[7mword\033[27m.\n"),
    (f"Only effect for this {Effect.HIDE}word{Effect.HIDE_OFF}.", "Only effect for this \033[8mword\033[28m.\n"),

    # String concatenation:
    ("I want both " + Color.RED + "colored and " + Effect.BLINK + "blinking" + Effect.BLINK_OFF + " text" + Color.OFF + " inside this paragraph", MIXED_PARAMETERS_MOCK_TEXT),

    # Multiple and mixed parameters inside string:
    (f"I want both {Color.RED}colored and {Effect.BLINK}blinking{Effect.BLINK_OFF} text{Color.OFF} inside this paragraph", MIXED_PARAMETERS_MOCK_TEXT),
])
def test_custom_text_effect(text: str, expected: str, capfd: object) -> None:
    print(text)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == expected
