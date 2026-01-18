# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.foreground.oklch import ColorOKLCH
from ...print.general import print_color


def oklch(text: str, lightness: float, chroma: float, hue: float) -> None:
    """Prints full line of custom OKLCH-colored text.

    Args:
        text (str): Text to be printed on colored background.
        lightness (float): Lightness value between `0.0` and `1.0` where `0` is black and `1` is white.
        chroma (float): Chroma value between `0.0` and `0.4`.
        hue (float): Number between `0` and `360` degrees.
    """

    color_oklch = ColorOKLCH(lightness, chroma, hue)
    print_color(text, color=color_oklch)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def oklch(self, text: str, lightness: float, chroma: float, hue: float) -> None:
        """Prints full line of custom OKLCH-colored text.

        Args:
            text (str): Text to be printed on colored background.
            lightness (float): Lightness value between `0.0` and `1.0` where `0` is black and `1` is white.
            chroma (float): Chroma value between `0.0` and `0.4`.
            hue (float): Number between `0` and `360` degrees.

        Example:
            ```python title="" linenums="1" hl_lines="3"
            from colorist import oklch

            oklch("I want this text in orange OKLCH colors", 0.71, 0.1, 31)
            ```

            How it appears in the terminal:

            <pre><code>% <span style="color: oklch(0.71 0.1 31)">I want this text in orange OKLCH colors</span></code></pre>
        """
