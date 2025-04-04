# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.foreground.rgb import ColorRGB
from ...print.general import print_color


def rgb(text: str, red: int, green: int, blue: int) -> None:
    """Prints full line of custom RGB-colored text. Values for red, green, blue can be between `0` and `255`."""

    color_rgb = ColorRGB(red, green, blue)
    print_color(text, color=color_rgb)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def rgb(self, text: str, red: int, green: int, blue: int) -> None:
        """Prints full line of custom RGB-colored text.

        Args:
            text (str): Text to be printed with color.
            red (int): Number between `0` and `255`.
            green (int): Number between `0` and `255`.
            blue (int): Number between `0` and `255`.

        Example:
            ```python title="" linenums="1" hl_lines="3"
            from colorist import rgb

            rgb("I want this text in blue RGB colors", 0, 128, 255)
            ```

            How it appears in the terminal:

            <pre><code>% <span style="color: rgb(0, 128, 255)">I want this text in blue RGB colors</span></code></pre>
        """
