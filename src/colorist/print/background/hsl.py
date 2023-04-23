# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.background.hsl import BgColorHSL
from ...print.general import print_color


def bg_hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Prints full line of text on custom HSL-colored background. Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    bg_color_hsl = BgColorHSL(hue, lightness, saturation)
    print_color(text, bg_color=bg_color_hsl)
