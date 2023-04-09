# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ...constants.ansi import RESET_ALL, AnsiColor, AnsiColorSelector
from ...helper.generate import ansi_standard_color_sequence
from ..abc.color import FgColor_ABC


class Color(FgColor_ABC):
    """Options for standard text colors. Implements ANSI escape codes for printing color, effects, and styling in the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    BLACK = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.BLACK)
    RED = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.RED)
    GREEN = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.GREEN)
    YELLOW = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.YELLOW)
    BLUE = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.BLUE)
    MAGENTA = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.MAGENTA)
    CYAN = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.CYAN)
    WHITE = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.WHITE)
    DEFAULT = ansi_standard_color_sequence(AnsiColorSelector.FOREGROUND, AnsiColor.DEFAULT)

    OFF = RESET_ALL
