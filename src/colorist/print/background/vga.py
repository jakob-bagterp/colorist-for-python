# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.vga import BgColorVGA
from ...print.general import print_color


def bg_vga(text: str, vga: int) -> None:
    """Prints full line of text on 8-bit VGA-colored background. Color values can be between `0` and `255`."""

    bg_color_vga = BgColorVGA(vga)
    print_color(text, bg_color=bg_color_vga)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_vga(self, text: str, vga: int) -> None:
        """Prints full line of text on 8-bit VGA-colored background.

        Args:
            text (str): Text to be printed on colored background.
            vga (int): Number between `0` and `255`.

        Example:
            ```python linenums="1"
            from colorist import vga

            bg_vga("I want this background in blue VGA colors", 33)
            ```

            How it appears in the terminal:

            <pre><code>% <span style="background-color: #0087ff">I want this background in blue VGA colors</span></code></pre>
        """
