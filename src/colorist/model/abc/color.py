# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC


class Color_ABC(ABC):
    """Abstract base class for standard ANSI color classes."""

    BLACK: str
    RED: str
    GREEN: str
    YELLOW: str
    BLUE: str
    MAGENTA: str
    CYAN: str
    WHITE: str
    DEFAULT: str

    OFF: str


class FgColor_ABC(Color_ABC):
    """Abstract base class for foreground classes of standard ANSI colors."""


class BgColor_ABC(Color_ABC):
    """Abstract base class for background classes of standard ANSI colors."""
