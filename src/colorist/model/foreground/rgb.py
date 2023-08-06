# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.rgb import RGB_ABC


class ColorRGB(RGB_ABC):
    """Class for custom RGB foreground text color."""

    def __init__(self, red: int, green: int, blue: int) -> None:
        """
        Args:
            red (int): Number between `0` and `255`.
            green (int): Number between `0` and `255`.
            blue (int): Number between `0` and `255`.

        Example:
            ```python linenums="1"
            from colorist import ColorRGB, BgColorRGB

            dusty_pink = ColorRGB(194, 145, 164)
            bg_steel_blue = BgColorRGB(70, 130, 180)

            print(f"I want to use {dusty_pink}dusty pink{dusty_pink.OFF} and {bg_steel_blue}steel blue{bg_steel_blue.OFF} colors inside this paragraph")
            ```

            How it appears in the terminal:

            ![Another example of text in RGB colors printed in a terminal window](../assets/images/examples/rgb_custom_text.png)
        """
        # TODO: Update code example to only use ColorRGB and not BgColorRGB.

        super().__init__(red, green, blue)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self)
