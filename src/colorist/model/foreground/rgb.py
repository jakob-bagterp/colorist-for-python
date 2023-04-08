from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.rgb import RGB_ABC


class ColorRGB(RGB_ABC):
    """Class for RGB foreground text color."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self)
