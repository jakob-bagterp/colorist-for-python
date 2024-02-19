# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from .. import helper
from ..model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ..model.background.bright_color import BgBrightColor
from ..model.background.color import BgColor
from ..model.effect import Effect
from ..model.foreground.bright_color import BrightColor
from ..model.foreground.color import Color


def effect_bold(text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
    """Prints full line of text with bold styling."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.BOLD, color)


def effect_dim(text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
    """Prints full line of text with dim styling."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.DIM, color)


def effect_underline(text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
    """Prints full line of text with underline styling."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.UNDERLINE, color)


def effect_blink(text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
    """Prints full line of text with blink effect."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.BLINK, color)


def effect_reverse(text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
    """Prints full line of text with reversed foreground and background color effect."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.REVERSE, color)


def effect_hide(text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
    """Prints full line of text with hide effect."""

    color = helper.print.normalize_input(color)
    helper.print.effect(text, Effect.HIDE, color)


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def effect_bold(self, text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
        """Prints full line of text with bold styling.

        Args:
            text (str): Text to be printed with bold styling.
            color (Color | BrightColor | BgColor | BgBrightColor | str | None, optional): Optionally add color to text.

        Example:
            ```python title="" linenums="1"
            from colorist import effect_bold, Color, BgColor

            effect_bold("This is BOLD")
            effect_bold("This is BOLD", Color.BLUE)
            effect_bold("This is BOLD", BgColor.RED)
            ```

            How it appears in the terminal:

            <pre><code>% <strong>This is BOLD</strong>
            % <span class="fg-blue"><strong>This is BOLD</strong></span>
            % <span class="bg-red"><strong>This is BOLD</strong></span></code></pre>
        """

    def effect_dim(self, text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
        """Prints full line of text with dim styling.

        Args:
            text (str): Text to be printed with dim effect.
            color (Color | BrightColor | BgColor | BgBrightColor | str | None, optional): Optionally add color to text.

        Example:
            ```python title="" linenums="1"
            from colorist import effect_dim, BrightColor, BgColor

            effect_dim("This is DIMMED")
            effect_dim("This is DIMMED", BrightColor.GREEN)
            effect_dim("This is DIMMED", BgColor.MAGENTA)
            ```

            How it appears in the terminal:

            <pre><code>% <span class="effect-dimmed">This is DIMMED</span>
            % <span class="effect-dimmed fg-bright-green">This is DIMMED</span>
            % <span class="effect-dimmed bg-magenta">This is DIMMED</span></code></pre>
        """

    def effect_underline(self, text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
        """Prints full line of text with underline styling.

        Args:
            text (str): Text to be printed with underline styling.
            color (Color | BrightColor | BgColor | BgBrightColor | str | None, optional): Optionally add color to text.

        Example:
            ```python title="" linenums="1"
            from colorist import effect_underline, Color, BgBrightColor

            effect_underline("This is UNDERLINED")
            effect_underline("This is UNDERLINED", Color.CYAN)
            effect_underline("This is UNDERLINED", BgBrightColor.BLUE)
            ```

            How it appears in the terminal:

            <pre><code>% <u>This is UNDERLINED</u>
            % <span class="fg-cyan"><u>This is UNDERLINED</u></span>
            % <span class="bg-bright-blue"><u>This is UNDERLINED</u></span></code></pre>
        """

    def effect_blink(self, text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
        """Prints full line of text with blink effect.

        Args:
            text (str): Text to be printed with blink effect.
            color (Color | BrightColor | BgColor | BgBrightColor | str | None, optional): Optionally add color to text.

        Example:
            ```python title="" linenums="1"
            from colorist import effect_blink, BrightColor, BgColor

            effect_blink("This is BLINKING")
            effect_blink("This is BLINKING", BrightColor.YELLOW)
            effect_blink("This is BLINKING", BgColor.GREEN)
            ```

            How it appears in the terminal:

            <pre><code>% <span class="effect-blinking">This is BLINKING</span>
            % <span class="effect-blinking fg-bright-yellow">This is BLINKING</span>
            % <span class="effect-blinking bg-green">This is BLINKING</span></code></pre>
        """

    def effect_reverse(self, text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
        """Prints full line of text with reversed foreground and background color effect.

        Args:
            text (str): Text to be printed with reverse effect.
            color (Color | BrightColor | BgColor | BgBrightColor | str | None, optional): Optionally add color to text.

        Example:
            ```python title="" linenums="1"
            from colorist import effect_reverse, Color, BgColor

            effect_reverse("This is REVERSED")
            effect_reverse("This is REVERSED", Color.CYAN)
            effect_reverse("This is REVERSED", BgColor.RED)
            ```

            How it appears in the terminal:

            <pre><code>% <span class="bg-bright-white">This is REVERSED</span>
            % <span class="bg-bright-cyan">This is REVERSED</span>
            % <span class="bg-bright-white"><span class="fg-red">This is REVERSED</span></span></code></pre>
        """

    def effect_hide(self, text: str, color: Color | BrightColor | BgColor | BgBrightColor | str | None = None) -> None:
        """Prints full line of text with hide effect.

        Args:
            text (str): Text to be printed with hide effect.
            color (Color | BrightColor | BgColor | BgBrightColor | str | None, optional): Optionally add color to text.

        Example:
            ```python title="" linenums="1"
            from colorist import effect_hide, Color, BgColor

            effect_hide("This is HIDDEN")
            effect_hide("This is HIDDEN", Color.BLUE)
            effect_hide("This is HIDDEN", BgColor.RED)
            ```

            How it appears in the terminal:

            <pre><code>% <span class="effect-hidden">This is HIDDEN</span>
            % <span class="effect-hidden fg-blue">This is HIDDEN</span>
            % <span class="bg-red"><span class="effect-hidden">This is HIDDEN</span></span></code></pre>
        """
