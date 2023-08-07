# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.foreground.bright_color import BrightColor


def bright_black(text: str) -> None:
    """Prints full line of bright black text."""

    helper.print.color(text, color=BrightColor.BLACK)


def bright_red(text: str) -> None:
    """Prints full line of bright red text."""

    helper.print.color(text, color=BrightColor.RED)


def bright_green(text: str) -> None:
    """Prints full line of bright green text."""

    helper.print.color(text, color=BrightColor.GREEN)


def bright_yellow(text: str) -> None:
    """Prints full line of bright yellow text."""

    helper.print.color(text, color=BrightColor.YELLOW)


def bright_blue(text: str) -> None:
    """Prints full line of bright blue text."""

    helper.print.color(text, color=BrightColor.BLUE)


def bright_magenta(text: str) -> None:
    """Prints full line of bright magenta text."""

    helper.print.color(text, color=BrightColor.MAGENTA)


def bright_cyan(text: str) -> None:
    """Prints full line of bright cyan text."""

    helper.print.color(text, color=BrightColor.CYAN)


def bright_white(text: str) -> None:
    """Prints full line of bright white text."""

    helper.print.color(text, color=BrightColor.WHITE)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bright_black(self, text: str) -> None:
        """Prints full line of bright black text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_red(self, text: str) -> None:
        """Prints full line of bright red text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_green(self, text: str) -> None:
        """Prints full line of bright green text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_yellow(self, text: str) -> None:
        """Prints full line of bright yellow text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_blue(self, text: str) -> None:
        """Prints full line of bright blue text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_magenta(self, text: str) -> None:
        """Prints full line of bright magenta text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_cyan(self, text: str) -> None:
        """Prints full line of bright cyan text.

        Args:
            text (str): Text to be printed with color.
        """

    def bright_white(self, text: str) -> None:
        """Prints full line of bright white text.

        Args:
            text (str): Text to be printed with color.
        """
