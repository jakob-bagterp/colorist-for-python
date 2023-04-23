# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.background.rgb import BgColorRGB
from ...print.general import print_color


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Prints full line of text on custom RGB-colored background. Values for red, green, blue can be between 0 and 255."""

    bg_color_rgb = BgColorRGB(red, green, blue)
    print_color(text, bg_color=bg_color_rgb)
