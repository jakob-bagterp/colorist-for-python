from . import helper
from .model.background_bright_color import BgBrightColor
from .model.background_color import BgColor
from .model.bright_color import BrightColor
from .model.color import Color
from .model.effect import Effect


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
    helper.print.color(text, bg_color=BgColor.GREEN)


def bg_yellow(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.YELLOW)


def bg_red(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.RED)


def bg_magenta(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.MAGENTA)


def bg_blue(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.BLUE)


def bg_cyan(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.CYAN)


def bg_white(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.WHITE)


def bg_black(text: str) -> None:
    helper.print.color(text, bg_color=BgColor.BLACK)


def bg_bright_green(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.GREEN)


def bg_bright_yellow(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.YELLOW)


def bg_bright_red(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.RED)


def bg_bright_magenta(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.MAGENTA)


def bg_bright_blue(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.BLUE)


def bg_bright_cyan(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.CYAN)


def bg_bright_white(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.WHITE)


def bg_bright_black(text: str) -> None:
    helper.print.color(text, bg_color=BgBrightColor.BLACK)


def effect_bold(text: str, color: Color | BrightColor | str = "") -> None:
    helper.print.effect(text, Effect.BOLD, color)


def effect_dim(text: str, color: Color | BrightColor | str = "") -> None:
    helper.print.effect(text, Effect.DIM, color)


def effect_underline(text: str, color: Color | BrightColor | str = "") -> None:
    helper.print.effect(text, Effect.UNDERLINE, color)


def effect_blink(text: str, color: Color | BrightColor | str = "") -> None:
    helper.print.effect(text, Effect.BLINK, color)


def effect_reverse(text: str, color: Color | BrightColor | str = "") -> None:
    helper.print.effect(text, Effect.REVERSE, color)


def effect_hide(text: str, color: Color | BrightColor | str = "") -> None:
    helper.print.effect(text, Effect.HIDE, color)


def rgb(text: str, red: int, green: int, blue: int) -> None:
    """Values for red, green, blue can be between 0 and 255."""

    helper.print.rgb(text, red, green, blue)


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Values for red, green, blue can be between 0 and 255."""

    helper.print.bg_rgb(text, red, green, blue)


def hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    red, green, blue = helper.convert.hsl_to_rgb(hue, lightness, saturation)
    helper.print.rgb(text, red, green, blue)


def bg_hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    red, green, blue = helper.convert.hsl_to_rgb(hue, lightness, saturation)
    helper.print.bg_rgb(text, red, green, blue)
