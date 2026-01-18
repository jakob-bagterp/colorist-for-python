# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.oklch import OKLCH_ABC


class ColorOKLCH(OKLCH_ABC):
    """Class for custom OKLCH foreground text color."""

    def __init__(self, lightness: float, chroma: float, hue: float) -> None:
        """
        Args:
            lightness (float): Lightness value between `0.0` and `1.0` where `0.0` is black and `1.0` is white.
            chroma (float): Chroma value between `0.0` and `0.4`.
            hue (float): Number between `0` and `360` degrees.

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from colorist import ColorOKLCH

            dusty_orange = ColorOKLCH(0.71, 0.1, 31)

            print(f"I want to use {dusty_orange}DUSTY ORANGE{dusty_orange.OFF} foreground color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span style="color: oklch(0.71 0.1 31)">DUSTY ORANGE</span> foreground color inside this paragraph</code></pre>
        """

        super().__init__(lightness, chroma, hue)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self._rgb)
