# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.foreground.color import Color


def black(text: str) -> None:
    """Prints full line of black text."""

    helper.print.color(text, color=Color.BLACK)


def red(text: str) -> None:
    """Prints full line of red text."""

    helper.print.color(text, color=Color.RED)


def green(text: str) -> None:
    """Prints full line of green text."""

    helper.print.color(text, color=Color.GREEN)


def yellow(text: str) -> None:
    """Prints full line of yellow text."""

    helper.print.color(text, color=Color.YELLOW)


def blue(text: str) -> None:
    """Prints full line of blue text."""

    helper.print.color(text, color=Color.BLUE)


def magenta(text: str) -> None:
    """Prints full line of magenta text."""

    helper.print.color(text, color=Color.MAGENTA)


def cyan(text: str) -> None:
    """Prints full line of cyan text."""

    helper.print.color(text, color=Color.CYAN)


def white(text: str) -> None:
    """Prints full line of white text."""

    helper.print.color(text, color=Color.WHITE)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def black(self, text: str) -> None:
        """Prints full line of black text.

        Args:
            text (str): Text to be printed with color.
        """

    def red(self, text: str) -> None:
        """Prints full line of red text.

        Args:
            text (str): Text to be printed with color.
        """

    def green(self, text: str) -> None:
        """Prints full line of green text.

        Args:
            text (str): Text to be printed with color.
        """

    def yellow(self, text: str) -> None:
        """Prints full line of yellow text.

        Args:
            text (str): Text to be printed with color.
        """

    def blue(self, text: str) -> None:
        """Prints full line of blue text.

        Args:
            text (str): Text to be printed with color.
        """

    def magenta(self, text: str) -> None:
        """Prints full line of magenta text.

        Args:
            text (str): Text to be printed with color.
        """

    def cyan(self, text: str) -> None:
        """Prints full line of cyan text.

        Args:
            text (str): Text to be printed with color.
        """

    def white(self, text: str) -> None:
        """Prints full line of white text.

        Args:
            text (str): Text to be printed with color.
        """
