# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from enum import Enum

from ..constants.ansi import RESET_ALL
from ..model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ..model.background.bright_color import BgBrightColor
from ..model.background.color import BgColor
from ..model.background.hex import BgColorHex
from ..model.background.hsl import BgColorHSL
from ..model.background.rgb import BgColorRGB
from ..model.background.vga import BgColorVGA
from ..model.effect import Effect
from ..model.foreground.bright_color import BrightColor
from ..model.foreground.color import Color
from ..model.foreground.hex import ColorHex
from ..model.foreground.hsl import ColorHSL
from ..model.foreground.rgb import ColorRGB
from ..model.foreground.vga import ColorVGA


def style_text(text: str,
               *styles: Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | Effect | str | None
               ) -> str:
    """Style text with various options for text and background colors, styling and effects."""

    def _get_style_value(style: Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | Effect | str | None) -> str:
        if style is None:
            return ""
        if isinstance(style, Enum):
            return str(style.value)
        return str(style)

    return f"{''.join(_get_style_value(style) for style in styles)}{text}{RESET_ALL}"


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def style_text(text: str,
                   *styles: Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | Effect | str | None
                   ) -> str:
        """Style text with various options for text and background colors, styling and effects.

        Args:
            text (str): The text to be styled.
            *styles (Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | Effect | str | None, optional): The text and/or background colors, styling and/or effects to be applied to the text.

        Returns:
            A new string with the text wrapped in the relevant ANSI escape codes, e.g. `style_text("APPROVED", Color.GREEN)` yields `\\033[32mAPPROVED\\033[0m`.

        Example:
            ```python
            from colorist import style_text, Color, Effect

            text = style_text("WARNING", Color.YELLOW, Effect.BOLD)
            print(text)
            ```

            How it appears in the terminal:

            <pre><code>% <span class="fg-yellow"><strong>WARNING</strong></span></code></pre>
        """
