# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ... import helper
from ...model.foreground.color import Color


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
