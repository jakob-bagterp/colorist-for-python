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

        Example:
            ```python title="" linenums="1"
            from colorist import black

            black("This is BLACK!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-black">This is BLACK!</span></code></pre>
        """

    def red(self, text: str) -> None:
        """Prints full line of red text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import red

            red("This is RED!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-red">This is RED!</span></code></pre>
        """

    def green(self, text: str) -> None:
        """Prints full line of green text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import green

            green("This is GREEN!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-green">This is GREEN!</span></code></pre>
        """

    def yellow(self, text: str) -> None:
        """Prints full line of yellow text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import yellow

            yellow("This is YELLOW!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-yellow">This is YELLOW!</span></code></pre>
        """

    def blue(self, text: str) -> None:
        """Prints full line of blue text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import blue

            blue("This is BLUE!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-blue">This is BLUE!</span></code></pre>
        """

    def magenta(self, text: str) -> None:
        """Prints full line of magenta text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import magenta

            magenta("This is MAGENTA!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-magenta">This is MAGENTA!</span></code></pre>
        """

    def cyan(self, text: str) -> None:
        """Prints full line of cyan text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import cyan

            cyan("This is CYAN!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-cyan">This is CYAN!</span></code></pre>
        """

    def white(self, text: str) -> None:
        """Prints full line of white text.

        Args:
            text (str): Text to be printed with color.

        Example:
            ```python title="" linenums="1"
            from colorist import white

            white("This is WHITE!")
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-white">This is WHITE!</span></code></pre>
        """
