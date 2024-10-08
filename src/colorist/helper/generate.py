# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from ..constants.ansi import (AnsiColor, AnsiColorSelector, AnsiEffect,
                              AnsiEffectSelector, AnsiRgbColorSelector,
                              AnsiVgaColorSelector)
from ..constants.ascii import AsciiEscapeCode
from ..model.abc.rgb import RGB_ABC
from ..model.abc.vga import VGA_ABC


def control_sequence_inducer(ascii_escape_code: AsciiEscapeCode) -> str:
    """Control Sequence Inducer (CSI) marks the beginning of a control sequence, e.g. "\\u1b[" in "\\u1b[31m"."""

    return f"{ascii_escape_code}["


def ansi_standard_color_sequence(selector: AnsiColorSelector | AnsiEffectSelector, value: AnsiColor | AnsiEffect, ascii_escape_code: AsciiEscapeCode = AsciiEscapeCode.OCTAL) -> str:
    """Generate standard ANSI color sequence, e.g. "\\u1b[31m"."""

    csi = control_sequence_inducer(ascii_escape_code)
    return f"{csi}{selector}{value}m"


def ansi_vga_color_sequence(selector: AnsiVgaColorSelector, vga: VGA_ABC, ascii_escape_code: AsciiEscapeCode = AsciiEscapeCode.OCTAL) -> str:
    """Generate ANSI 8-bit VGA color sequence, e.g. "\\u1b[38;5;166m"."""

    csi = control_sequence_inducer(ascii_escape_code)
    return f"{csi}{selector};{vga.vga}m"


def ansi_rgb_color_sequence(selector: AnsiRgbColorSelector, rgb: RGB_ABC, ascii_escape_code: AsciiEscapeCode = AsciiEscapeCode.OCTAL) -> str:
    """Generate ANSI 16-bit RGB color sequence, e.g. "\\u1b[38;2;r;g;bm"."""

    csi = control_sequence_inducer(ascii_escape_code)
    return f"{csi}{selector};{rgb.red};{rgb.green};{rgb.blue}m"
