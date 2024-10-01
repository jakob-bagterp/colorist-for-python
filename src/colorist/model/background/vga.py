# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiVgaColorSelector
from ..abc.vga import VGA_ABC


class BgColorVGA(VGA_ABC):
    """Class for custom 8-bit VGA background color instances."""

    def __init__(self, vga: int) -> None:
        """
        Args:
            vga (int): Number between `0` and `255`.

        Example:
            ```python linenums="1"
            from colorist import BgColorVGA

            bg_lime_green = BgColorVGA(120)

            print(f"I want to use {bg_lime_green}lime green{bg_lime_green.OFF} background color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span style="background-color: #87ff87">lime green</span> background color inside this paragraph</code></pre>
        """

        super().__init__(vga)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_vga_color_sequence(AnsiVgaColorSelector.BACKGROUND, self)
