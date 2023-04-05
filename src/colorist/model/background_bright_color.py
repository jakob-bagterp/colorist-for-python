from ..constants.ansi import RESET_ALL
from .abc.color import Color_ABC


class BgBrightColor(Color_ABC):
    """Options for bright background colors (not standard, but mostly supported). Implements ANSI escape codes for printing color, effects, and styling to the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    GREEN = "\033[102m"
    YELLOW = "\033[103m"
    RED = "\033[101m"
    MAGENTA = "\033[105m"
    BLUE = "\033[104m"
    CYAN = "\033[106m"
    WHITE = "\033[107m"
    BLACK = "\033[100m"
    DEFAULT = "\033[99m"
    OFF = RESET_ALL
