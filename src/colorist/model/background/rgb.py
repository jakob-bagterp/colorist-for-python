# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.rgb import RGB_ABC


class BgColorRGB(RGB_ABC):
    """Class for custom 16-bit RGB background color instances."""

    def __init__(self, red: int, green: int, blue: int) -> None:
        """
        Args:
            red (int): Number between `0` and `255`.
            green (int): Number between `0` and `255`.
            blue (int): Number between `0` and `255`.

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from colorist import BgColorRGB

            bg_steel_blue = BgColorRGB(70, 130, 180)

            print(f"I want to use {bg_steel_blue}STEEL BLUE{bg_steel_blue.OFF} background color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span class="text-contrast" style="background-color: rgb(70, 130, 180)">STEEL BLUE</span> background color inside this paragraph</code></pre>
        """

        super().__init__(red, green, blue)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self)
