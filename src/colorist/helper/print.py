# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ..constants.ansi import RESET_ALL
from ..model.abc.color import BgColor_ABC, FgColor_ABC
from ..model.abc.effect import Effect_ABC


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
