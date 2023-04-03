from enum import Enum, unique


@unique
class AsciiEscapeCode(Enum):
    """Control Sequence Introducer (CSI) marks the beginning of a control sequence, e.g. "\\u1b[31m"."""

    OCTAL = "\033"
    """Supported in: Bash, C, Python 3."""

    HEX = "\x1b"
    """Supported in: Bash, C, Python 3."""

    UNICODE = "\u001b"
    """Supported in: Bash, Python 3."""

    def __str__(self) -> str:
        return str(self.value)
