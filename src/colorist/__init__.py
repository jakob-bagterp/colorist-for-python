__all__ = []

from enum import Enum

class Color(Enum):
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[35m"
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
