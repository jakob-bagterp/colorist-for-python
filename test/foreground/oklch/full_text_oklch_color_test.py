# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import pytest
import terminal

from colorist import oklch


@pytest.mark.parametrize("text, oklch_input, rgb_expected", [
    ("random text", (0, 0, 0), (0, 0, 0)),
    ("random text", (1, 0, 0), (255, 255, 255)),
    ("random text", (0.5, 0.2, 0.0), (179, 5, 94)),
    ("random text", (0.7, 0.1, 45.0), (210, 138, 105)),
    ("random text", (0.7, 0.1, 45), (210, 138, 105)),
])
def test_full_text_oklch_color(text: str, oklch_input: tuple[float, float, float], rgb_expected: tuple[int, int, int], capfd: object) -> None:
    lightness, chroma, hue = oklch_input
    oklch(text, lightness, chroma, hue)
    terminal_output = terminal.get_output(capfd)
    red, green, blue = rgb_expected
    assert terminal_output == f"\033[38;2;{red};{green};{blue}m{text}\033[0m\n"
