# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC, abstractmethod

from ... import helper
from ...constants.ansi import RESET_ALL
from ...helper.error import message_for_hex_value_error
from ...helper.validate import is_valid_hex_value
from ..foreground.rgb import ColorRGB
from .rgb import RGB_ABC


class Hex_ABC(ABC):
    """Abstract base class for custom Hex color instances."""

    OFF = RESET_ALL

    __slots__ = ["hex", "_rgb", "_ansi_code"]

    def __init__(self, hex: str) -> None:
        if not is_valid_hex_value(hex):
            raise ValueError(message_for_hex_value_error(hex))

        self.hex: str = hex.lower()

        self._rgb: RGB_ABC = self.convert_hex_to_rgb()
        self._ansi_code: str = self.generate_ansi_code()

    def __str__(self) -> str:
        return self._ansi_code

    def __repr__(self) -> str:
        return f"Hex: #{self.hex.lstrip('#')}"

    def convert_hex_to_rgb(self) -> RGB_ABC:
        """Method to convert Hex to RGB color."""

        red, green, blue = helper.convert.hex_to_rgb(self.hex)
        return ColorRGB(red, green, blue)

    @abstractmethod
    def generate_ansi_code(self) -> str:
        """Method to generate ANSI RGB color sequence."""

        raise NotImplementedError  # pragma: no cover
