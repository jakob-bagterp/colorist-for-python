# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.foreground.hsl import ColorHSL
from ...print.general import print_color


def hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Prints full line of custom HSL-colored text. Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    color_hsl = ColorHSL(hue, lightness, saturation)
    print_color(text, color=color_hsl)
