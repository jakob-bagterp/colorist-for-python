# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper


def bg_hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Prints full line of text on custom HSL-colored background. Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    red, green, blue = helper.convert.hsl_to_rgb(hue, lightness, saturation)
    helper.print.bg_rgb(text, red, green, blue)
