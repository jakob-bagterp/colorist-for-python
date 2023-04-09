from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.rgb import RGB_ABC


class BgColorRGB(RGB_ABC):
    """Class for custom RGB background color."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self)
