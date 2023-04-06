from abc import ABC, abstractmethod


class RGB_ABC(ABC):
    """Abstract base class for RGB color classes."""

    __slots__ = ["red", "green", "blue", "_ansi_code"]

    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self._ansi_code: str = self.generate_ansi_code()

    def __str__(self) -> str:
        return self._ansi_code

    def __repr__(self) -> str:
        return f"R: {self.red}, G: {self.green}, B: {self.blue}"

    @abstractmethod
    def generate_ansi_code(self) -> str:
        """Method to generate ANSI RGB color sequence."""

        raise NotImplementedError
