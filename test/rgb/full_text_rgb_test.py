import pytest
import terminal

from colorist import rgb


@pytest.mark.parametrize("text, red, green, blue", [
    ("random text", 0, 0, 0),
    ("random text", 255, 255, 255),
    ("random text", 135, 17, 221),
])
def test_full_text_rgb(text: str, red: int, green: int, blue: int, capfd: object) -> None:
    rgb(text, red, green, blue)
    terminal_output = terminal.get_output(capfd)
    assert terminal_output == f"\033[38;2;{red};{green};{blue}m{text}\033[0m\n"
