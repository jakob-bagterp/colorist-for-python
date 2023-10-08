# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hsl import HSL_ABC


class ColorHSL(HSL_ABC):
    """Class for custom HSL foreground text color."""

    def __init__(self, hue: float, saturation: float, lightness: float) -> None:
        """
        Args:
            hue (float): Number between `0` and `360` degrees.
            saturation (float): Percentage between `0` and `100` %.
            lightness (float): Percentage between `0` and `100` %.

        Example:
            ```python linenums="1"
            from colorist import ColorHSL

            mustard_green = ColorHSL(60, 56, 43)

            print(f"I want to use {mustard_green}mustard green{mustard_green.OFF} color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span style="color: hsl(60, 56%, 43%)">mustard green</span> color inside this paragraph</code></pre>
        """

        super().__init__(hue, saturation, lightness)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self._rgb)
