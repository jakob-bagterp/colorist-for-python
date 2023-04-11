# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...constants.ansi import RESET_ALL, AnsiColor, AnsiColorSelector
from ...helper.generate import ansi_standard_color_sequence
from ..abc.color import BgColor_ABC


class BgBrightColor(BgColor_ABC):
    """Options for bright background colors (not standard, but mostly supported). Implements ANSI escape codes for printing color, effects, and styling in the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    BLACK = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.BLACK)
    RED = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.RED)
    GREEN = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.GREEN)
    YELLOW = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.YELLOW)
    BLUE = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.BLUE)
    MAGENTA = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.MAGENTA)
    CYAN = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.CYAN)
    WHITE = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.WHITE)
    DEFAULT = ansi_standard_color_sequence(AnsiColorSelector.BRIGHT_BACKGROUND, AnsiColor.DEFAULT)

    OFF = RESET_ALL
