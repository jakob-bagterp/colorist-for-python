from enum import Enum, unique

from .color import Color


@unique
class BgColor(Enum):
    """Options for standard background colors."""

    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    RED = "\033[41m"
    MAGENTA = "\033[45m"
    BLUE = "\033[44m"
    CYAN = "\033[46m"
    WHITE = "\033[47m"
    BLACK = "\033[40m"
    DEFAULT = "\033[49m"
    OFF = Color.OFF

    def __str__(self) -> str:
        return str(self.value)
