# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ...model.background.bright_color import BgBrightColor


def bg_bright_black(text: str) -> None:
    """Prints full line of text on bright black background."""

    helper.print.color(text, bg_color=BgBrightColor.BLACK)


def bg_bright_red(text: str) -> None:
    """Prints full line of text on bright red background."""

    helper.print.color(text, bg_color=BgBrightColor.RED)


def bg_bright_green(text: str) -> None:
    """Prints full line of text on bright green background."""

    helper.print.color(text, bg_color=BgBrightColor.GREEN)


def bg_bright_yellow(text: str) -> None:
    """Prints full line of text on bright yellow background."""

    helper.print.color(text, bg_color=BgBrightColor.YELLOW)


def bg_bright_blue(text: str) -> None:
    """Prints full line of text on bright blue background."""

    helper.print.color(text, bg_color=BgBrightColor.BLUE)


def bg_bright_magenta(text: str) -> None:
    """Prints full line of text on bright magenta background."""

    helper.print.color(text, bg_color=BgBrightColor.MAGENTA)


def bg_bright_cyan(text: str) -> None:
    """Prints full line of text on bright cyan background."""

    helper.print.color(text, bg_color=BgBrightColor.CYAN)


def bg_bright_white(text: str) -> None:
    """Prints full line of text on bright white background."""

    helper.print.color(text, bg_color=BgBrightColor.WHITE)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def bg_bright_black(self, text: str) -> None:
        """Prints full line of text on bright black background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_red(self, text: str) -> None:
        """Prints full line of text on bright red background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_green(self, text: str) -> None:
        """Prints full line of text on bright green background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_yellow(self, text: str) -> None:
        """Prints full line of text on bright yellow background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_blue(self, text: str) -> None:
        """Prints full line of text on bright blue background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_magenta(self, text: str) -> None:
        """Prints full line of text on bright magenta background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_cyan(self, text: str) -> None:
        """Prints full line of text on bright cyan background.

        Args:
            text (str): Text to be printed on colored background.
        """

    def bg_bright_white(self, text: str) -> None:
        """Prints full line of text on bright white background.

        Args:
            text (str): Text to be printed on colored background.
        """
