# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiVgaColorSelector
from ..abc.vga import VGA_ABC


class ColorVGA(VGA_ABC):
    """Class for custom 8-bit VGA foreground text color."""

    def __init__(self, vga: int) -> None:
        """
        Args:
            vga (int): Number between `0` and `255`.

        Example:
            ```python linenums="1"
            from colorist import ColorVGA

            lime_green = ColorVGA(120)

            print(f"I want to use {lime_green}lime green{lime_green.OFF} color inside this paragraph")
            ```

            How it appears in the terminal:

            <pre><code>% I want to use <span style="color: #87ff87">lime green</span> color inside this paragraph</code></pre>
        """

        super().__init__(vga)

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_vga_color_sequence(AnsiVgaColorSelector.FOREGROUND, self)
