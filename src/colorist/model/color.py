from ..constants.ansi import RESET_ALL
from .abc.color import FgColor_ABC


class Color(FgColor_ABC):
    """Options for standard colors. Implements ANSI escape codes for printing color, effects, and styling to the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BLACK = "\033[30m"
    DEFAULT = "\033[39m"
    OFF = RESET_ALL
