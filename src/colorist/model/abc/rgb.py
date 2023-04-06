from abc import ABC, abstractmethod

from ...constants.ansi import RESET_ALL
from ...helper.error import message_for_rgb_value_error
from ...helper.validate import is_valid_rgb_value


class RGB_ABC(ABC):
    """Abstract base class for RGB color classes."""

    __slots__ = ["red", "green", "blue", "OFF", "_ansi_code"]

    def __init__(self, red: int, green: int, blue: int) -> None:
        if not is_valid_rgb_value(red):
            raise ValueError(message_for_rgb_value_error("red", red))
        if not is_valid_rgb_value(green):
            raise ValueError(message_for_rgb_value_error("green", green))
        if not is_valid_rgb_value(blue):
            raise ValueError(message_for_rgb_value_error("blue", blue))

        self.red: int = red
        self.green: int = green
        self.blue: int = blue

        self._ansi_code: str = self.generate_ansi_code()
        self.OFF = RESET_ALL

    def __str__(self) -> str:
        return self._ansi_code

    def __repr__(self) -> str:
        return f"R: {self.red}, G: {self.green}, B: {self.blue}"

    @abstractmethod
    def generate_ansi_code(self) -> str:
        """Method to generate ANSI RGB color sequence."""

        raise NotImplementedError
