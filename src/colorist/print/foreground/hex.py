# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper


def hex(text: str, hex: str) -> None:
    """Prints full line of text in Hex color. Expects valid Hex color value, for instance #B4FBB8 or B4FBB8, #B4F or B4F."""

    red, green, blue = helper.convert.hex_to_rgb(hex)
    helper.print.rgb(text, red, green, blue)
