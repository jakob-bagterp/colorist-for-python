# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hex import Hex_ABC


class ColorHex(Hex_ABC):
    """Class for custom foreground text defined in Hex color."""

    def __init__(self, hex: str) -> None:
        """
        Args:
            hex (str): Hex color value, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`.

        Example:
            ```python linenums="1"
            from colorist import ColorHex, BgColorHex

            watermelon_red = ColorHex("#ff5733")
            bg_mint_green = BgColorHex("#99ff99")

            print(f"I want to use {watermelon_red}watermelon pink{watermelon_red.OFF} and {bg_mint_green}mint green{bg_mint_green.OFF} colors inside this paragraph")
            ```

            How it appears in the terminal:

            ![Another example of text in Hex colors printed in a terminal window](../assets/images/examples/hex_custom_text.png)
        """
        # TODO: Update code example to only use ColorHex and not BgColorHex.

        super().__init__(hex)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self._rgb)
