from ... import helper
from ...model.background_bright_color import BgBrightColor


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
