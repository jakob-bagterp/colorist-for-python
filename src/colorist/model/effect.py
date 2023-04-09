# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ..constants.ansi import RESET_ALL, AnsiEffect, AnsiEffectSelector
from ..helper.generate import ansi_standard_color_sequence
from .abc.effect import Effect_ABC


class Effect(Effect_ABC):
    """Options for effects and styling of text. Implements ANSI escape codes for effects and styling in the terminal.

    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""

    BOLD = ansi_standard_color_sequence(AnsiEffectSelector.ON, AnsiEffect.BOLD)
    DIM = ansi_standard_color_sequence(AnsiEffectSelector.ON, AnsiEffect.DIM)
    UNDERLINE = ansi_standard_color_sequence(AnsiEffectSelector.ON, AnsiEffect.UNDERLINE)
    BLINK = ansi_standard_color_sequence(AnsiEffectSelector.ON, AnsiEffect.BLINK)
    REVERSE = ansi_standard_color_sequence(AnsiEffectSelector.ON, AnsiEffect.REVERSE)
    HIDE = ansi_standard_color_sequence(AnsiEffectSelector.ON, AnsiEffect.HIDE)

    BOLD_OFF = ansi_standard_color_sequence(AnsiEffectSelector.OFF, AnsiEffect.BOLD)
    DIM_OFF = ansi_standard_color_sequence(AnsiEffectSelector.OFF, AnsiEffect.DIM)
    UNDERLINE_OFF = ansi_standard_color_sequence(AnsiEffectSelector.OFF, AnsiEffect.UNDERLINE)
    BLINK_OFF = ansi_standard_color_sequence(AnsiEffectSelector.OFF, AnsiEffect.BLINK)
    REVERSE_OFF = ansi_standard_color_sequence(AnsiEffectSelector.OFF, AnsiEffect.REVERSE)
    HIDE_OFF = ansi_standard_color_sequence(AnsiEffectSelector.OFF, AnsiEffect.HIDE)

    OFF = RESET_ALL
