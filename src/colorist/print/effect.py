# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from .. import helper
from ..model.effect import Effect
from ..model.foreground.bright_color import BrightColor
from ..model.foreground.color import Color


def effect_bold(text: str, color: Color | BrightColor | str = "") -> None:
    """Prints full line of text with bold styling."""

    helper.print.effect(text, Effect.BOLD, color)


def effect_dim(text: str, color: Color | BrightColor | str = "") -> None:
    """Prints full line of text with dim styling."""

    helper.print.effect(text, Effect.DIM, color)


def effect_underline(text: str, color: Color | BrightColor | str = "") -> None:
    """Prints full line of text with underline styling."""

    helper.print.effect(text, Effect.UNDERLINE, color)


def effect_blink(text: str, color: Color | BrightColor | str = "") -> None:
    """Prints full line of text with blink effect."""

    helper.print.effect(text, Effect.BLINK, color)


def effect_reverse(text: str, color: Color | BrightColor | str = "") -> None:
    """Prints full line of text with reversed foreground and background color effect."""

    helper.print.effect(text, Effect.REVERSE, color)


def effect_hide(text: str, color: Color | BrightColor | str = "") -> None:
    """Prints full line of text with hide effect."""

    helper.print.effect(text, Effect.HIDE, color)
