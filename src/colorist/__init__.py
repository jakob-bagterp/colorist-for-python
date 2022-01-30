__all__ = ["bright_color", "color", "effect"]

from .version import __version__

from typing import Union
from .color import Color
from .bright_color import BrightColor
from .effect import Effect

def print_color(text: str, color: Union[Color, BrightColor]) -> None:
    print(f"{color}{text}{Color.OFF}")

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

def print_effect(text: str, effect: Effect, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print(f"{color}{effect}{text}{Effect.OFF}")

def effect_bold(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect(text, Effect.BOLD, color)

def effect_dim(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect(text, Effect.DIM, color)

def effect_underline(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect(text, Effect.UNDERLINE, color)

def effect_blink(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect(text, Effect.BLINK, color)

def effect_reverse(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect(text, Effect.REVERSE, color)

def effect_hide(text: str, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print_effect(text, Effect.HIDE, color)
