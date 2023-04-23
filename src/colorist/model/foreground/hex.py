# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...constants.ansi import AnsiRgbColorSelector
from ..abc.hex import Hex_ABC


class ColorHex(Hex_ABC):
    """Class for custom foreground text defined in Hex color. Expects valid Hex color value, for instance #B4FBB8 or B4FBB8, #B4F or B4F."""

    def generate_ansi_code(self) -> str:
        return helper.generate.ansi_rgb_color_sequence(AnsiRgbColorSelector.FOREGROUND, self._rgb)
