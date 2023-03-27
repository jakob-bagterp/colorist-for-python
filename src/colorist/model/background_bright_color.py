from .background_color import BgColor
from .color import Color


class BgBrightColor():
    """Options for bright background colors. Implements ANSI escape codes for printing color, effects, and styling to the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

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
