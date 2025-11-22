# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ..constants.ansi import RESET_ALL
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
               *args: Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | Effect | str | None
               ) -> str:
    """Style text with various options for text and background color, styling and effects.

    Args:
        text (str): The text to be styled.
        *args (Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | Effect | str | None, optional): The text and/or background colors, styling and/or effects to be applied to the text.

    Returns:
        str: A new text string wrapped in the appropriate ANSI escape codes.

    Example:
        ```python
        text = f"{style_text("WARNING", Color.YELLOW, Effect.BOLD)}: This is an example."
        ```
    """

    return f"{''.join(map(str, args))}{text}{RESET_ALL}"
