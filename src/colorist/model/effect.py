from .color import Color


class Effect():
    """Options for effects and styling. Implements ANSI escape codes for printing color, effects, and styling to the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDE = "\033[8m"

    BOLD_OFF = "\033[21m"
    DIM_OFF = "\033[22m"
    UNDERLINE_OFF = "\033[24m"
    BLINK_OFF = "\033[25m"
    REVERSE_OFF = "\033[27m"
    HIDE_OFF = "\033[28m"
    OFF = Color.OFF
