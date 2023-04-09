# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Prints full line of text on custom RGB-colored background. Values for red, green, blue can be between 0 and 255."""

    helper.print.bg_rgb(text, red, green, blue)
