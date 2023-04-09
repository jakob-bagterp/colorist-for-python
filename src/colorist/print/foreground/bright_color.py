# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.foreground.bright_color import BrightColor


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
