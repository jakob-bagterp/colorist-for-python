from ..constants.ansi import SGR_END, AnsiColor, AnsiColorSelector
from ..constants.ascii import AsciiEscapeCode


def control_sequence_inducer(ascii_escape_code: AsciiEscapeCode) -> str:
    """Control Sequence Inducer (CSI) marks the beginning of a control sequence, e.g. "\\u1b[31m"."""

    return f"{ascii_escape_code}["


def ansi_standard_color_sequence(selector: AnsiColorSelector, color: AnsiColor, ascii_escape_code: AsciiEscapeCode = AsciiEscapeCode.OCTAL) -> str:
    """Generate standard ANSI color sequence, e.g. "\\u1b[31m"."""

    csi = control_sequence_inducer(ascii_escape_code)
    return f"{csi}{selector}{color}{SGR_END}"
