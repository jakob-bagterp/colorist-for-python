# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.foreground.hex import ColorHex
from ...print.general import print_color


def hex(text: str, hex: str) -> None:
    """Prints full line of text in Hex color. Expects valid Hex color value, for instance #B4FBB8 or B4FBB8, #B4F or B4F."""

    color_hex = ColorHex(hex)
    print_color(text, color=color_hex)
