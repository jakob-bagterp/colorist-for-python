# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC, abstractmethod

from ... import helper
from ...constants.ansi import RESET_ALL
from ...helper.error import (message_for_hue_value_error,
                             message_for_oklch_chroma_value_error,
                             message_for_percentage_as_decimal_value_error)
from ...helper.validate import (is_valid_hue_value,
                                is_valid_oklch_chroma_value,
                                is_valid_percentage_as_decimal)
from ..foreground.rgb import ColorRGB
from .rgb import RGB_ABC


class OKLCH_ABC(ABC):
    """Abstract base class for custom OKLCH color instances."""

    OFF = RESET_ALL

    __slots__ = ["chroma", "hue", "lightness", "_rgb", "_ansi_code"]

    def __init__(self, lightness: float, chroma: float, hue: float):
        if not is_valid_percentage_as_decimal(lightness):
            raise ValueError(message_for_percentage_as_decimal_value_error("lightness", lightness))
        if not is_valid_oklch_chroma_value(chroma):
            raise ValueError(message_for_oklch_chroma_value_error(chroma))
        if not is_valid_hue_value(hue):
            raise ValueError(message_for_hue_value_error(hue))
        self.hue: float = hue
        self.chroma: float = chroma
        self.lightness: float = lightness

        self._rgb: RGB_ABC = self.convert_oklch_to_srgb()
        self._ansi_code: str = self.generate_ansi_code()

    def __str__(self) -> str:
        return self._ansi_code

    def __repr__(self) -> str:
        return f"L: {self.lightness}, C: {self.chroma}, H: {self.hue}"

    def convert_oklch_to_srgb(self) -> RGB_ABC:
        """Method to convert OKLCH to RGB color."""

        red, green, blue = helper.convert.oklch_to_srgb(self.lightness, self.chroma, self.hue)
        return ColorRGB(red, green, blue)

    @abstractmethod
    def generate_ansi_code(self) -> str:
        """Method to generate ANSI RGB color sequence."""

        raise NotImplementedError  # pragma: no cover
