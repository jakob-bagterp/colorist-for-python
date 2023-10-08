# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.hsl import BgColorHSL
from ...print.general import print_color


def bg_hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Prints full line of text on custom HSL-colored background. Value for hue can be number between `0` and `360` degrees, while saturation and lightness can be a percentage between `0` and `100` %."""

    bg_color_hsl = BgColorHSL(hue, lightness, saturation)
    print_color(text, bg_color=bg_color_hsl)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_hsl(self, text: str, hue: float, saturation: float, lightness: float) -> None:
        """Prints full line of text on custom HSL-colored background.

        Args:
            text (str): Text to be printed on colored background.
            hue (float): Number between `0` and `360` degrees.
            saturation (float): Percentage between `0` and `100` %.
            lightness (float): Percentage between `0` and `100` %.

        Example:
            ```python linenums="1"
            from colorist import bg_hsl

            bg_hsl("I want this background in green HSL colors", 120, 50, 50)
            ```

            How it appears in the terminal:

            <pre><code>% <span style="background-color: hsl(120, 50%, 50%)">I want this background in green HSL colors</span></code></pre>
        """
