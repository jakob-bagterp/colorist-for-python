from enum import Enum, unique
from .color import Color

@unique
class BrightColor(Enum):
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BLACK   = "\033[90m"
    DEFAULT = Color.DEFAULT
    RESET   = Color.RESET

    def __str__(self):
        return str(self.value)
