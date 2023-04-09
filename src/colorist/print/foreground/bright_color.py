# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.foreground.bright_color import BrightColor


def bright_black(text: str) -> None:
    """Prints full line of bright black text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.BLACK)


def bright_red(text: str) -> None:
    """Prints full line of bright red text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.RED)


def bright_green(text: str) -> None:
    """Prints full line of bright green text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.GREEN)


def bright_yellow(text: str) -> None:
    """Prints full line of bright yellow text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.YELLOW)


def bright_blue(text: str) -> None:
    """Prints full line of bright blue text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.BLUE)


def bright_magenta(text: str) -> None:
    """Prints full line of bright magenta text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.MAGENTA)


def bright_cyan(text: str) -> None:
    """Prints full line of bright cyan text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.CYAN)


def bright_white(text: str) -> None:
    """Prints full line of bright white text. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, color=BrightColor.WHITE)
