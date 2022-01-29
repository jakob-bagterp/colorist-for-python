from enum import Enum, unique
from .color import Color

@unique
class Effect(Enum):
    BOLD      = "\033[1m"
    DIM       = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK     = "\033[5m"
    REVERSE   = "\033[7m"
    HIDE      = "\033[8m"

    RESET_BOLD      = "\033[21m"
    RESET_DIM       = "\033[22m"
    RESET_UNDERLINE = "\033[24m"
    RESET_BLINK     = "\033[25m"
    RESET_REVERSE   = "\033[27m"
    RESET_HIDE      = "\033[28m"
    RESET_ALL       = Color.RESET

    def __str__(self):
        return str(self.value)
