from enum import Enum, unique

@unique
class Color(Enum):
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    RED     = "\033[31m"
    MAGENTA = "\033[35m"
    BLUE    = "\033[34m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    BLACK   = "\033[30m"
    DEFAULT = "\033[39m"
    RESET   = "\033[0m"
