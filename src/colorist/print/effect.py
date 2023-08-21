# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from .. import helper
from ..model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ..model.effect import Effect
from ..model.foreground.bright_color import BrightColor
from ..model.foreground.color import Color


def effect_bold(text: str, color: Color | BrightColor | str | None = None) -> None:
    """Prints full line of text with bold styling."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.BOLD, color)


def effect_dim(text: str, color: Color | BrightColor | str | None = None) -> None:
    """Prints full line of text with dim styling."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.DIM, color)


def effect_underline(text: str, color: Color | BrightColor | str | None = None) -> None:
    """Prints full line of text with underline styling."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.UNDERLINE, color)


def effect_blink(text: str, color: Color | BrightColor | str | None = None) -> None:
    """Prints full line of text with blink effect."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.BLINK, color)


def effect_reverse(text: str, color: Color | BrightColor | str | None = None) -> None:
    """Prints full line of text with reversed foreground and background color effect."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.REVERSE, color)


def effect_hide(text: str, color: Color | BrightColor | str | None = None) -> None:
    """Prints full line of text with hide effect."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.HIDE, color)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def effect_bold(self, text: str, color: Color | BrightColor | str | None = None) -> None:
        """Prints full line of text with bold styling.

        Args:
            text (str): Text to be printed with bold styling.
            color (Color | BrightColor | str | None, optional): Optionally add color to text.
        """

    def effect_dim(self, text: str, color: Color | BrightColor | str | None = None) -> None:
        """Prints full line of text with dim styling.

        Args:
            text (str): Text to be printed with dim effect.
            color (Color | BrightColor | str | None, optional): Optionally add color to text.
        """

    def effect_underline(self, text: str, color: Color | BrightColor | str | None = None) -> None:
        """Prints full line of text with underline styling.

        Args:
            text (str): Text to be printed with underline styling.
            color (Color | BrightColor | str | None, optional): Optionally add color to text.
        """

    def effect_blink(self, text: str, color: Color | BrightColor | str | None = None) -> None:
        """Prints full line of text with blink effect.

        Args:
            text (str): Text to be printed with blink effect.
            color (Color | BrightColor | str | None, optional): Optionally add color to text.
        """

    def effect_reverse(self, text: str, color: Color | BrightColor | str | None = None) -> None:
        """Prints full line of text with reversed foreground and background color effect.

        Args:
            text (str): Text to be printed with reverse effect.
            color (Color | BrightColor | str | None, optional): Optionally add color to text.
        """

    def effect_hide(self, text: str, color: Color | BrightColor | str | None = None) -> None:
        """Prints full line of text with hide effect.

        Args:
            text (str): Text to be printed with hide effect.
            color (Color | BrightColor | str | None, optional): Optionally add color to text.
        """
