# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.hex import BgColorHex
from ...print.general import print_color


def bg_hex(text: str, hex: str) -> None:
    """Prints full line of text on colored background defined in Hex color. Expects valid Hex color value with or without hashtag, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`."""

    bg_color_hex = BgColorHex(hex)
    print_color(text, bg_color=bg_color_hex)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_hex(self, text: str, hex: str) -> None:
        """Prints full line of text on colored background defined in Hex color.

        Args:
            text (str): Text to be printed on colored background.
            hex (str): Hex color value with or without hashtag, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`.

        Example:
            ```python linenums="1"
            from colorist import bg_hex

            bg_hex("I want this background in coral Hex colors", "#ff7f50")
            ```

            How it appears in the terminal:

            <pre><code>% <span style="background-color: #ff7f50">I want this background in coral Hex colors</span></code></pre>
        """
