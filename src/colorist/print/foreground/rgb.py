# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper


def rgb(text: str, red: int, green: int, blue: int) -> None:
    """Prints full line of custom RGB-colored text. Values for red, green, blue can be between 0 and 255."""

    helper.print.rgb(text, red, green, blue)
