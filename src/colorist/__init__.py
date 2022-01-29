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
    DEFAULT = "\033[39m"
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
    DEFAULT = Color.DEFAULT
    RESET   = Color.RESET

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

def print_effect_with_color(text: str, effect: Effect, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print(f"{color}{effect}{text}{Effect.RESET_ALL}")

def effect_bold(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect_with_color(text, Effect.BOLD, color)

def effect_dim(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect_with_color(text, Effect.DIM, color)

def effect_underline(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect_with_color(text, Effect.UNDERLINE, color)

def effect_blink(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect_with_color(text, Effect.BLINK, color)

def effect_reverse(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect_with_color(text, Effect.REVERSE, color)

def effect_hide(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect_with_color(text, Effect.HIDE, color)
