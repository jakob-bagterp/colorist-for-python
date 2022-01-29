__all__ = []

from .version import __version__

from enum import Enum, unique
from typing import Union

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
    RESET   = "\033[0m"

def print_color(text: str, color: Union[Color, BrightColor]) -> None:
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

def bright_green(text: str) -> None:
    print_color(text, BrightColor.GREEN)

def bright_yellow(text: str) -> None:
    print_color(text, BrightColor.YELLOW)

def bright_red(text: str) -> None:
    print_color(text, BrightColor.RED)

def bright_magenta(text: str) -> None:
    print_color(text, BrightColor.MAGENTA)

def bright_blue(text: str) -> None:
    print_color(text, BrightColor.BLUE)

def bright_cyan(text: str) -> None:
    print_color(text, BrightColor.CYAN)

def bright_white(text: str) -> None:
    print_color(text, BrightColor.WHITE)

def bright_black(text: str) -> None:
    print_color(text, BrightColor.BLACK)
