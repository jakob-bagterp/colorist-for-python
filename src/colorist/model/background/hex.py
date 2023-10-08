# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hex import Hex_ABC


class BgColorHex(Hex_ABC):
    """Class for custom background defined in Hex color."""

    def __init__(self, hex: str) -> None:
        """
        Args:
            hex (str): Hex color value with or without hashtag, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`.

        Example:
            ```python linenums="1"
            from colorist import BgColorHex

            bg_mint_green = BgColorHex("#99ff99")

            print(f"I want to use {bg_mint_green}mint green{bg_mint_green.OFF} background color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span style="background-color: #99ff99">mint green</span> background color inside this paragraph</code></pre>
        """

        super().__init__(hex)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self._rgb)
