from enum import Enum, unique

from .background_color import BgColor
from .color import Color


@unique
class BgBrightColor(Enum):
    """Options for bright background colors."""

    GREEN = "\033[102m"
    YELLOW = "\033[103m"
    RED = "\033[101m"
    MAGENTA = "\033[105m"
    BLUE = "\033[104m"
    CYAN = "\033[106m"
    WHITE = "\033[107m"
    BLACK = "\033[100m"
    DEFAULT = BgColor.DEFAULT
    OFF = Color.OFF

    def __str__(self) -> str:
        return str(self.value)
