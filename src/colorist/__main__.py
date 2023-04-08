from . import helper
from .model.background_bright_color import BgBrightColor
from .model.bright_color import BrightColor
from .model.color import Color
from .model.effect import Effect


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
