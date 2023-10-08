# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.rgb import BgColorRGB
from ...print.general import print_color


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Prints full line of text on custom RGB-colored background. Values for red, green, blue can be between `0` and `255`."""

    bg_color_rgb = BgColorRGB(red, green, blue)
    print_color(text, bg_color=bg_color_rgb)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_rgb(self, text: str, red: int, green: int, blue: int) -> None:
        """Prints full line of text on custom RGB-colored background.

        Args:
            text (str): Text to be printed on colored background.
            red (int): Number between `0` and `255`.
            green (int): Number between `0` and `255`.
            blue (int): Number between `0` and `255`.

        Example:
            ```python linenums="1"
            from colorist import bg_rgb

            bg_rgb("I want this background in blue RGB colors", 0, 128, 255)
            ```

            How it appears in the terminal:

            <pre><code>% <span style="background-color: rgb(0, 128, 255)">I want this background in blue RGB colors</span></code></pre>
        """
