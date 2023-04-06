import pytest
import terminal

from colorist import hsl


@pytest.mark.parametrize("text, hsl_input, rgb_expected", [
    ("random text", (100, 20, 80), (37, 91, 10)),
    ("random text", (250, 50, 55), (80, 57, 197)),  # Other converters say (102, 82, 197)
    ("random text", (360, 30, 70), (130, 22, 22)),  # Other converters say (201, 155, 155)
    ("random text", (0, 100, 0), (255, 255, 255)),
    ("random text", (0, 0, 0), (0, 0, 0)),
])
def test_full_text_hsl_color(text: str, hsl_input: tuple[float, float, float], rgb_expected: tuple[int, int, int], capfd: object) -> None:
    hue, saturation, lightness = hsl_input
    hsl(text, hue, saturation, lightness)
    terminal_output = terminal.get_output(capfd)
    red, green, blue = rgb_expected
    assert terminal_output == f"\033[38;2;{red};{green};{blue}m{text}\033[0m\n"
