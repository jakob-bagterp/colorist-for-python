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
            from colorist import BgColorHSL

            bg_steel_gray = BgColorHSL(190, 2, 49)

            print(f"I want to use {bg_steel_gray}steel gray{bg_steel_gray.OFF} background color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span style="background-color: hsl(190, 2%, 49%)">steel gray</span> background color inside this paragraph</code></pre>
        """

        super().__init__(hue, saturation, lightness)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self._rgb)
