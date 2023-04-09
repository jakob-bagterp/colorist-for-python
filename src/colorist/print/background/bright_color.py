# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.background.bright_color import BgBrightColor


def bg_bright_black(text: str) -> None:
    """Prints full line of text on bright black background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.BLACK)


def bg_bright_red(text: str) -> None:
    """Prints full line of text on bright red background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.RED)


def bg_bright_green(text: str) -> None:
    """Prints full line of text on bright green background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.GREEN)


def bg_bright_yellow(text: str) -> None:
    """Prints full line of text on bright yellow background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.YELLOW)


def bg_bright_blue(text: str) -> None:
    """Prints full line of text on bright blue background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.BLUE)


def bg_bright_magenta(text: str) -> None:
    """Prints full line of text on bright magenta background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.MAGENTA)


def bg_bright_cyan(text: str) -> None:
    """Prints full line of text on bright cyan background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.CYAN)


def bg_bright_white(text: str) -> None:
    """Prints full line of text on bright white background. Note that bright colors are supported by many terminals, but not all as bright colors aren't part of the standard ANSI colors."""

    helper.print.color(text, bg_color=BgBrightColor.WHITE)
