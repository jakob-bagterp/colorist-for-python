# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.foreground.vga import ColorVGA
from ...print.general import print_color


def vga(text: str, vga: int) -> None:
    """Prints full line of 8-bit VGA-colored text. Color values can be between `0` and `255`."""

    color_vga = ColorVGA(vga)
    print_color(text, color=color_vga)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def vga(self, text: str, vga: int) -> None:
        """Prints full line of 8-bit VGA-colored text.

        Args:
            text (str): Text to be printed with color.
            vga (int): Number between `0` and `255`.

        Example:
            ```python linenums="1"
            from colorist import vga

            vga("I want this text in blue VGA colors", 33)
            ```

            How it appears in the terminal:

            <pre><code>% <span style="color: #0087ff">I want this text in blue VGA colors</span></code></pre>
        """
