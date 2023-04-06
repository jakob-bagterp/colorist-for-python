from .. import helper
from ..constants.ansi import AnsiRgbColorSelector
from .abc.hsl import HSL_ABC


class ColorHSL(HSL_ABC):
    """Class for HSL foreground text color."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self._rgb)


class BgColorHSL(HSL_ABC):
    """Class for HSL background color."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self._rgb)