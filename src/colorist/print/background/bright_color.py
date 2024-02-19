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

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_black

            bg_bright_black("This is BRIGHT BLACK background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-black">This is BRIGHT BLACK background!</span></code></pre>
        """

    def bg_bright_red(self, text: str) -> None:
        """Prints full line of text on bright red background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_red

            bg_bright_red("This is BRIGHT RED background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-red">This is BRIGHT RED background!</span></code></pre>
        """

    def bg_bright_green(self, text: str) -> None:
        """Prints full line of text on bright green background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_green

            bg_bright_green("This is BRIGHT GREEN background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-green">This is BRIGHT GREEN background!</span></code></pre>
        """

    def bg_bright_yellow(self, text: str) -> None:
        """Prints full line of text on bright yellow background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_yellow

            bg_bright_yellow("This is BRIGHT YELLOW background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-yellow">This is BRIGHT YELLOW background!</span></code></pre>
        """

    def bg_bright_blue(self, text: str) -> None:
        """Prints full line of text on bright blue background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_blue

            bg_bright_blue("This is BRIGHT BLUE background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-blue">This is BRIGHT BLUE background!</span></code></pre>
        """

    def bg_bright_magenta(self, text: str) -> None:
        """Prints full line of text on bright magenta background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_magenta

            bg_bright_magenta("This is BRIGHT MAGENTA background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-magenta">This is BRIGHT MAGENTA background!</span></code></pre>
        """

    def bg_bright_cyan(self, text: str) -> None:
        """Prints full line of text on bright cyan background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_cyan

            bg_bright_cyan("This is BRIGHT CYAN background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-cyan">This is BRIGHT CYAN background!</span></code></pre>
        """

    def bg_bright_white(self, text: str) -> None:
        """Prints full line of text on bright white background.

        Args:
            text (str): Text to be printed on colored background.

        Example:
            ```python title="" linenums="1"
            from colorist import bg_bright_white

            bg_bright_white("This is BRIGHT WHITE background!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-white">This is BRIGHT WHITE background!</span></code></pre>
        """
