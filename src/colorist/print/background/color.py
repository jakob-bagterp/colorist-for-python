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

        Example:
            ```python title="" linenums="1"
            from colorist import bg_black

            bg_black("This is BLACK background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-black">This is BLACK background!</span></code></pre>
        """

    def bg_red(self, text: str) -> None:
        """Prints full line of text on red background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_red

            bg_red("This is RED background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-red">This is RED background!</span></code></pre>
        """

    def bg_green(self, text: str) -> None:
        """Prints full line of text on green background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_green

            bg_green("This is GREEN background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-green">This is GREEN background!</span></code></pre>
        """

    def bg_yellow(self, text: str) -> None:
        """Prints full line of text on yellow background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_yellow

            bg_yellow("This is YELLOW background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-yellow">This is YELLOW background!</span></code></pre>
        """

    def bg_blue(self, text: str) -> None:
        """Prints full line of text on blue background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_blue

            bg_blue("This is BLUE background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-blue">This is BLUE background!</span></code></pre>
        """

    def bg_magenta(self, text: str) -> None:
        """Prints full line of text on magenta background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_magenta

            bg_magenta("This is MAGENTA background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-magenta">This is MAGENTA background!</span></code></pre>
        """

    def bg_cyan(self, text: str) -> None:
        """Prints full line of text on cyan background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_cyan

            bg_cyan("This is CYAN background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-cyan">This is CYAN background!</span></code></pre>
        """

    def bg_white(self, text: str) -> None:
        """Prints full line of text on white background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"

            from colorist import bg_white

            bg_white("This is WHITE background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-white">This is WHITE background!</span></code></pre>
        """
