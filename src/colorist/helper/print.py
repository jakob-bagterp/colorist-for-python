# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ..constants.ansi import RESET_ALL
from ..model.abc.color import BgColor_ABC, FgColor_ABC
from ..model.abc.effect import Effect_ABC
from ..model.abc.hex import Hex_ABC
from ..model.abc.hsl import HSL_ABC
from ..model.abc.rgb import RGB_ABC


def color(text: str, color: FgColor_ABC | str = "", bg_color: BgColor_ABC | str = "") -> None:
    """Helper function to print a full line of colored text (options for standard ANSI colors in both foreground and background) in the terminal."""

    print(f"{bg_color}{color}{text}{RESET_ALL}")


def effect(text: str, effect: Effect_ABC | str, color: FgColor_ABC | str = "") -> None:
    """Helper function to print a full line of text with custom effect in the terminal."""

    print(f"{color}{effect}{text}{RESET_ALL}")


def rgb(text: str, red: int, green: int, blue: int) -> None:
    """Helper function to print a full line of text in custom RGB foreground colors in the terminal."""

    print(f"\033[38;2;{red};{green};{blue}m{text}{RESET_ALL}")


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Helper function to print a full line of text in custom RGB background colors in the terminal."""

    print(f"\033[48;2;{red};{green};{blue}m{text}{RESET_ALL}")


def normalize_input(input: FgColor_ABC | BgColor_ABC | RGB_ABC | HSL_ABC | Hex_ABC | Effect_ABC | None) -> str:
    """Normalize and convert color classes to string of ANSI escape code for print methods, especially converting None values to empty string."""

    return str(input) if input is not None else ""
