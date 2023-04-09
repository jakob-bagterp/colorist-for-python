# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hsl import HSL_ABC


class BgColorHSL(HSL_ABC):
    """Class for custom HSL background color."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.BACKGROUND, self._rgb)
