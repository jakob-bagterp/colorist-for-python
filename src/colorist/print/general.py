# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ..constants.ansi import RESET_ALL
from ..model.background.bright_color import BgBrightColor
from ..model.background.color import BgColor
from ..model.background.hex import BgColorHex
from ..model.background.hsl import BgColorHSL
from ..model.background.rgb import BgColorRGB
from ..model.effect import Effect
from ..model.foreground.bright_color import BrightColor
from ..model.foreground.color import Color
from ..model.foreground.hex import ColorHex
from ..model.foreground.hsl import ColorHSL
from ..model.foreground.rgb import ColorRGB


def print_color(text: str,
                color: Color | BrightColor | ColorRGB | ColorHSL | ColorHex | None = None,
                bg_color: BgColor | BgBrightColor | BgColorRGB | BgColorHSL | BgColorHex | None = None,
                effect: Effect | None = None
                ) -> None:
    """Prints full line of text with various options for text and background color, styling and effects."""

    color_str = str(color) if color is not None else ""
    bg_color_str = str(bg_color) if bg_color is not None else ""
    effect_str = str(effect) if bg_color is not None else ""

    print(f"{color_str}{bg_color_str}{effect_str}{text}{RESET_ALL}")
