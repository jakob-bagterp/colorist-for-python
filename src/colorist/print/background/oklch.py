# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.oklch import BgColorOKLCH
from ...print.general import print_color


def bg_oklch(text: str, lightness: float, chroma: float, hue: float) -> None:
    """Prints full line of text on custom OKLCH-colored background.

    Args:
        text (str): Text to be printed on colored background.
        lightness (float): Lightness value between `0.0` and `1.0` where `0` is black and `1` is white.
        chroma (float): Chroma value between `0.0` and `0.4`.
        hue (float): Number between `0` and `360` degrees.
    """

    bg_color_oklch = BgColorOKLCH(lightness, chroma, hue)
    print_color(text, bg_color=bg_color_oklch)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_oklch(self, text: str, lightness: float, chroma: float, hue: float) -> None:
        """Prints full line of text on custom OKLCH-colored background.

        Args:
            text (str): Text to be printed on colored background.
            lightness (float): Lightness value between `0.0` and `1.0` where `0` is black and `1` is white.
            chroma (float): Chroma value between `0.0` and `0.4`.
            hue (float): Number between `0` and `360` degrees.

        Example:
            ```python title="" linenums="1" hl_lines="3"
            from colorist import bg_oklch

            bg_oklch("I want this background in green OKLCH colors", 0.54, 0.15, 141)
            ```

            How it appears in the terminal:

            <pre><code>% <span class="text-contrast" style="background-color: oklch(0.54 0.15 141)">I want this background in green OKLCH colors</span></code></pre>
        """
