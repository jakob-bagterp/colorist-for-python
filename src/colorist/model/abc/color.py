from abc import ABC


class Color_ABC(ABC):
    """Abstract base class for standard ANSI color classes."""

    __slots__ = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "DEFAULT", "OFF"]

    def __init__(self) -> None:
        self.BLACK: str
        self.RED: str
        self.GREEN: str
        self.YELLOW: str
        self.BLUE: str
        self.MAGENTA: str
        self.CYAN: str
        self.WHITE: str
        self.DEFAULT: str
        self.OFF: str


class FgColor_ABC(Color_ABC):
    """Abstract base class for foreground classes of standard ANSI colors."""


class BgColor_ABC(Color_ABC):
    """Abstract base class for background classes of standard ANSI colors."""
