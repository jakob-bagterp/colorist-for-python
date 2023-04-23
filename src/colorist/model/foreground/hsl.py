# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hsl import HSL_ABC


class ColorHSL(HSL_ABC):
    """Class for custom HSL foreground text color. Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self._rgb)
