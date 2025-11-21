# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from .. import helper
from ..constants.ansi import RESET_ALL
from ..model.abc.color import Color_ABC
from ..model.abc.hex import Hex_ABC
from ..model.abc.hsl import HSL_ABC
from ..model.abc.rgb import RGB_ABC
from ..model.abc.vga import VGA_ABC
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


def print_color(text: str,
                color: Color | BrightColor | ColorVGA | ColorRGB | ColorHSL | ColorHex | str | None = None,
                bg_color: BgColor | BgBrightColor | BgColorVGA | BgColorRGB | BgColorHSL | BgColorHex | str | None = None,
                effect: Effect | str | None = None
                ) -> None:
    """Prints full line of text with various options for text and background color, styling and effects."""

    color_str = helper.print.normalize_input(color)
    bg_color_str = helper.print.normalize_input(bg_color)
    effect_str = helper.print.normalize_input(effect)

    print(f"{color_str}{bg_color_str}{effect_str}{text}{RESET_ALL}")


def style_text(text: str,
               *args: Color_ABC | Hex_ABC | RGB_ABC | HSL_ABC | VGA_ABC | Effect | str
               ) -> str:
    """Applies arbitrary text and background color, styling and/or effects to a given string.

    Args:
        text (str): The text to be styled.
        *args (Color_ABC | Hex_ABC | Effect | str): Arbitrary number of optional effect parameters.

    Returns:
        str: The new string wrapped in the appropriate ANSI escape codes.

    ## Example
    ```python
    text = f"{style_text("WARNING", Color.YELLOW, Effect.BOLD)}: This is an example."
    ```
    """
    return "".join(map(str, args)) + text + RESET_ALL
