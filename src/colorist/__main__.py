from . import helper
from .model.background_bright_color import BgBrightColor
from .model.background_color import BgColor
from .model.bright_color import BrightColor
from .model.color import Color
from .model.effect import Effect


def green(text: str) -> None:
    helper.print.color(text, color=Color.GREEN)


def yellow(text: str) -> None:
    helper.print.color(text, color=Color.YELLOW)


def red(text: str) -> None:
    helper.print.color(text, color=Color.RED)


def magenta(text: str) -> None:
    helper.print.color(text, color=Color.MAGENTA)


def blue(text: str) -> None:
    helper.print.color(text, color=Color.BLUE)


def cyan(text: str) -> None:
    helper.print.color(text, color=Color.CYAN)


def white(text: str) -> None:
    helper.print.color(text, color=Color.WHITE)


def black(text: str) -> None:
    helper.print.color(text, color=Color.BLACK)


def bright_green(text: str) -> None:
    helper.print.color(text, color=BrightColor.GREEN)


def bright_yellow(text: str) -> None:
    helper.print.color(text, color=BrightColor.YELLOW)


def bright_red(text: str) -> None:
    helper.print.color(text, color=BrightColor.RED)


def bright_magenta(text: str) -> None:
    helper.print.color(text, color=BrightColor.MAGENTA)


def bright_blue(text: str) -> None:
    helper.print.color(text, color=BrightColor.BLUE)


def bright_cyan(text: str) -> None:
    helper.print.color(text, color=BrightColor.CYAN)


def bright_white(text: str) -> None:
    helper.print.color(text, color=BrightColor.WHITE)


def bright_black(text: str) -> None:
    helper.print.color(text, color=BrightColor.BLACK)


def bg_green(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.GREEN)


def bg_yellow(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.YELLOW)


def bg_red(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.RED)


def bg_magenta(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.MAGENTA)


def bg_blue(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.BLUE)


def bg_cyan(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.CYAN)


def bg_white(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.WHITE)


def bg_black(text: str) -> None:
    helper.print.color(text, bgcolor=BgColor.BLACK)


def bg_bright_green(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.GREEN)


def bg_bright_yellow(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.YELLOW)


def bg_bright_red(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.RED)


def bg_bright_magenta(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.MAGENTA)


def bg_bright_blue(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.BLUE)


def bg_bright_cyan(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.CYAN)


def bg_bright_white(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.WHITE)


def bg_bright_black(text: str) -> None:
    helper.print.color(text, bgcolor=BgBrightColor.BLACK)


def effect_bold(text: str, color: Color | BrightColor = Color.DEFAULT) -> None:
    helper.print.effect(text, Effect.BOLD, color)


def effect_dim(text: str, color: Color | BrightColor = Color.DEFAULT) -> None:
    helper.print.effect(text, Effect.DIM, color)


def effect_underline(text: str, color: Color | BrightColor = Color.DEFAULT) -> None:
    helper.print.effect(text, Effect.UNDERLINE, color)


def effect_blink(text: str, color: Color | BrightColor = Color.DEFAULT) -> None:
    helper.print.effect(text, Effect.BLINK, color)


def effect_reverse(text: str, color: Color | BrightColor = Color.DEFAULT) -> None:
    helper.print.effect(text, Effect.REVERSE, color)


def effect_hide(text: str, color: Color | BrightColor = Color.DEFAULT) -> None:
    helper.print.effect(text, Effect.HIDE, color)
