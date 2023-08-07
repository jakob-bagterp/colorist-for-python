# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hsl import HSL_ABC


class BgColorHSL(HSL_ABC):
    """Class for custom HSL background color."""

    def __init__(self, hue: float, saturation: float, lightness: float) -> None:
        """
        Args:
            hue (float): Number between `0` and `360` degrees.
            saturation (float): Percentage between `0` and `100` %.
            lightness (float): Percentage between `0` and `100` %.

        Example:
            ```python linenums="1"
            from colorist import ColorHSL, BgColorHSL

            mustard_green = ColorHSL(60, 56, 43)
            bg_steel_gray = BgColorHSL(190, 2, 49)

            print(f"I want to use {mustard_green}mustard green{mustard_green.OFF} and {bg_steel_gray}steel blue{bg_steel_gray.OFF} colors inside this paragraph")
            ```

            How it appears in the terminal:

            ![Another example of text in HSL colors printed in a terminal window](../assets/images/examples/hsl_custom_text.png)
        """
        # TODO: Update code example to only use BgColorHSL and not ColorHSL.

        super().__init__(hue, saturation, lightness)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self._rgb)
