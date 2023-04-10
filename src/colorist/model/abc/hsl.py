# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC, abstractmethod

from ... import helper
from ...constants.ansi import RESET_ALL
from ...helper.error import (message_for_hsl_hue_value_error,
                             message_for_hsl_percentage_value_error)
from ...helper.validate import is_valid_hsl_hue, is_valid_percentage
from ..foreground.rgb import ColorRGB
from .rgb import RGB_ABC


class HSL_ABC(ABC):
    """Abstract base class for custom HSL color instances."""

    OFF = RESET_ALL

    __slots__ = ["hue", "saturation", "lightness", "_rgb", "_ansi_code"]

    def __init__(self, hue: float, saturation: float, lightness: float) -> None:
        if not is_valid_hsl_hue(hue):
            raise ValueError(message_for_hsl_hue_value_error(hue))
        if not is_valid_percentage(saturation):
            raise ValueError(message_for_hsl_percentage_value_error("saturation", saturation))
        if not is_valid_percentage(lightness):
            raise ValueError(message_for_hsl_percentage_value_error("lightness", lightness))

        self.hue: float = hue
        self.saturation: float = saturation
        self.lightness: float = lightness

        self._rgb: RGB_ABC = self.convert_hsl_to_rgb()
        self._ansi_code: str = self.generate_ansi_code()

    def __str__(self) -> str:
        return self._ansi_code

    def __repr__(self) -> str:
        return f"H: {self.hue}, S: {self.saturation}, L: {self.lightness}"

    def convert_hsl_to_rgb(self) -> RGB_ABC:
        """Method to convert HSL to RGB color."""

        red, green, blue = helper.convert.hsl_to_rgb(self.hue, self.saturation, self.lightness)
        return ColorRGB(red, green, blue)

    @abstractmethod
    def generate_ansi_code(self) -> str:
        """Method to generate ANSI RGB color sequence."""

        raise NotImplementedError  # pragma: no cover
