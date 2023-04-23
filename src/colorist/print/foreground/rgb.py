# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.foreground.rgb import ColorRGB
from ...print.general import print_color


def rgb(text: str, red: int, green: int, blue: int) -> None:
    """Prints full line of custom RGB-colored text. Values for red, green, blue can be between 0 and 255."""

    color_rgb = ColorRGB(red, green, blue)
    print_color(text, color=color_rgb)
