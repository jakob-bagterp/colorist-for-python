# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC, abstractmethod

from ...constants.ansi import RESET_ALL
from ...helper.error import message_for_vga_value_error
from ...helper.validate import is_valid_vga_value


class VGA_ABC(ABC):
    """Abstract base class for custom 8-bit VGA color instances."""

    OFF = RESET_ALL

    __slots__ = ["vga", "_ansi_code"]

    def __init__(self, vga: int) -> None:
        if not is_valid_vga_value(vga):
            raise ValueError(message_for_vga_value_error(vga))

        self.vga: int = vga

        self._ansi_code: str = self.generate_ansi_code()

    def __str__(self) -> str:
        return self._ansi_code

    def __repr__(self) -> str:
        return f"VGA: {self.vga}"

    @abstractmethod
    def generate_ansi_code(self) -> str:
        """Method to generate ANSI VGA color sequence."""

        raise NotImplementedError  # pragma: no cover
