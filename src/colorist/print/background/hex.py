# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...model.background.hex import BgColorHex
from ...print.general import print_color


def bg_hex(text: str, hex: str) -> None:
    """Prints full line of text on colored background defined in Hex color. Expects valid Hex color value, for instance #B4FBB8 or B4FBB8, #B4F or B4F."""

    bg_color_hex = BgColorHex(hex)
    print_color(text, bg_color=bg_color_hex)
