# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from .. import helper
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
                color: Color | BrightColor | ColorRGB | ColorHSL | ColorHex | str | None = None,
                bg_color: BgColor | BgBrightColor | BgColorRGB | BgColorHSL | BgColorHex | str | None = None,
                effect: Effect | str | None = None
                ) -> None:
    """Prints full line of text with various options for text and background color, styling and effects."""

    color_str = helper.print.normalize_input(color)
    bg_color_str = helper.print.normalize_input(bg_color)
    effect_str = helper.print.normalize_input(effect)

    print(f"{color_str}{bg_color_str}{effect_str}{text}{RESET_ALL}")
