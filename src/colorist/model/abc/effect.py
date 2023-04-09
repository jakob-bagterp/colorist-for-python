from abc import ABC


class Effect_ABC(ABC):
    """Abstract base class for standard ANSI color classes."""

    __slots__ = ["BOLD", "DIM", "UNDERLINE", "BLINK", "REVERSE", "HIDE",
                 "BOLD_OFF", "DIM_OFF", "UNDERLINE_OFF", "BLINK_OFF", "REVERSE_OFF", "HIDE_OFF",
                 "OFF"]

    BOLD: str
    DIM: str
    UNDERLINE: str
    BLINK: str
    REVERSE: str
    HIDE: str

    BOLD_OFF: str
    DIM_OFF: str
    UNDERLINE_OFF: str
    BLINK_OFF: str
    REVERSE_OFF: str
    HIDE_OFF: str

    OFF: str
