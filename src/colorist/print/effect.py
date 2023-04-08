from .. import helper
from ..model.bright_color import BrightColor
from ..model.color import Color
from ..model.effect import Effect


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
