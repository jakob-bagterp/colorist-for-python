__all__ = []

from .version import __version__

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
    RESET   = "\033[0m"

def print_color(text: str, color: Color) -> None:
    print(f"{color}{text}{Color.RESET}")

def green(text: str) -> None:
    print_color(text, Color.GREEN)

def yellow(text: str) -> None:
    print_color(text, Color.YELLOW)

def red(text: str) -> None:
    print_color(text, Color.RED)

def magenta(text: str) -> None:
    print_color(text, Color.MAGENTA)

def blue(text: str) -> None:
    print_color(text, Color.BLUE)

def cyan(text: str) -> None:
    print_color(text, Color.CYAN)

def white(text: str) -> None:
    print_color(text, Color.WHITE)

def black(text: str) -> None:
    print_color(text, Color.BLACK)
