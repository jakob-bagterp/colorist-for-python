from ..constants.ansi import RESET_ALL
from .abc.color import FgColor_ABC


class BrightColor(FgColor_ABC):
    """Options for bright colors (not standard, but mostly supported). Implements ANSI escape codes for printing color, effects, and styling to the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[90m"
    DEFAULT = "\033[99m"
    OFF = RESET_ALL
