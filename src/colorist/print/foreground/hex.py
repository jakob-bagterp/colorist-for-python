# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.foreground.hex import ColorHex
from ...print.general import print_color


def hex(text: str, hex: str) -> None:
    """Prints full line of text in Hex color. Expects valid Hex color value, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`."""

    color_hex = ColorHex(hex)
    print_color(text, color=color_hex)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def hex(self, text: str, hex: str) -> None:
        """Prints full line of text in Hex color.

        Args:
            text (str): Text to be printed with color.
            hex (str): Hex color value, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`.

        Example:
            ```python linenums="1"
            from colorist import hex, bg_hex

            hex("I want this text in coral Hex colors", "#ff7f50")
            bg_hex("I want this background in coral Hex colors", "#ff7f50")
            ```

            How it appears in the terminal:

            ![Example of text in Hex colors printed in a terminal window](../assets/images/examples/hex_full_text.png)
        """
        # TODO: Update code example to only use hex() and not bg_hex().
