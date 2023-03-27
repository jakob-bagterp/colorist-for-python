from .color import Color


class BgColor():
    """Options for standard background colors. Implements ANSI escape codes for printing color, effects, and styling to the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

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
