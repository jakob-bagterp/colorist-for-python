# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.background.color import BgColor


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
