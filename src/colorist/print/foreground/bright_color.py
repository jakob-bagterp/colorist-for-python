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

        Example:
            ```python title="" linenums="1"
            from colorist import bright_black

            bright_black("This is BRIGHT BLACK!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-black">This is BRIGHT BLACK!</span></code></pre>
        """

    def bright_red(self, text: str) -> None:
        """Prints full line of bright red text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import bright_red

            bright_red("This is BRIGHT RED!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-red">This is BRIGHT RED!</span></code></pre>
        """

    def bright_green(self, text: str) -> None:
        """Prints full line of bright green text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"

            from colorist import bright_green

            bright_green("This is BRIGHT GREEN!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-green">This is BRIGHT GREEN!</span></code></pre>
        """

    def bright_yellow(self, text: str) -> None:
        """Prints full line of bright yellow text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import bright_yellow

            bright_yellow("This is BRIGHT YELLOW!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-yellow">This is BRIGHT YELLOW!</span></code></pre>
        """

    def bright_blue(self, text: str) -> None:
        """Prints full line of bright blue text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import bright_blue

            bright_blue("This is BRIGHT BLUE!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-blue">This is BRIGHT BLUE!</span></code></pre>
        """

    def bright_magenta(self, text: str) -> None:
        """Prints full line of bright magenta text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import bright_magenta

            bright_magenta("This is BRIGHT MAGENTA!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-magenta">This is BRIGHT MAGENTA!</span></code></pre>
        """

    def bright_cyan(self, text: str) -> None:
        """Prints full line of bright cyan text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import bright_cyan

            bright_cyan("This is BRIGHT CYAN!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-cyan">This is BRIGHT CYAN!</span></code></pre>
        """

    def bright_white(self, text: str) -> None:
        """Prints full line of bright white text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import bright_white

            bright_white("This is BRIGHT WHITE!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-bright-white">This is BRIGHT WHITE!</span></code></pre>
        """
