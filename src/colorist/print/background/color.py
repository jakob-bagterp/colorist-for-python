# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.color import BgColor


def bg_black(text: str) -> None:
    """Prints full line of text on black background."""

    helper.print.color(text, bg_color=BgColor.BLACK)


def bg_red(text: str) -> None:
    """Prints full line of text on red background."""

    helper.print.color(text, bg_color=BgColor.RED)


def bg_green(text: str) -> None:
    """Prints full line of text on green background."""

    helper.print.color(text, bg_color=BgColor.GREEN)


def bg_yellow(text: str) -> None:
    """Prints full line of text on yellow background."""

    helper.print.color(text, bg_color=BgColor.YELLOW)


def bg_blue(text: str) -> None:
    """Prints full line of text on blue background."""

    helper.print.color(text, bg_color=BgColor.BLUE)


def bg_magenta(text: str) -> None:
    """Prints full line of text on magenta background."""

    helper.print.color(text, bg_color=BgColor.MAGENTA)


def bg_cyan(text: str) -> None:
    """Prints full line of text on cyan background."""

    helper.print.color(text, bg_color=BgColor.CYAN)


def bg_white(text: str) -> None:
    """Prints full line of text on white background."""

    helper.print.color(text, bg_color=BgColor.WHITE)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_black(self, text: str) -> None:
        """Prints full line of text on black background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_red(self, text: str) -> None:
        """Prints full line of text on red background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_green(self, text: str) -> None:
        """Prints full line of text on green background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_yellow(self, text: str) -> None:
        """Prints full line of text on yellow background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_blue(self, text: str) -> None:
        """Prints full line of text on blue background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_magenta(self, text: str) -> None:
        """Prints full line of text on magenta background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_cyan(self, text: str) -> None:
        """Prints full line of text on cyan background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_white(self, text: str) -> None:
        """Prints full line of text on white background.

        Args:
            text (str): Text to be printed on colored background.
        """
