from abc import ABC


class Effect_ABC(ABC):
    """Abstract base class for standard ANSI color classes."""

    __slots__ = ["BOLD", "DIM", "UNDERLINE", "BLINK", "REVERSE", "HIDE",
                 "BOLD_OFF", "DIM_OFF", "UNDERLINE_OFF", "BLINK_OFF", "REVERSE_OFF", "HIDE_OFF",
                 "OFF"]

    def __init__(self) -> None:
        self.BOLD: str
        self.DIM: str
        self.UNDERLINE: str
        self.BLINK: str
        self.REVERSE: str
        self.HIDE: str

        self.BOLD_OFF: str
        self.DIM_OFF: str
        self.UNDERLINE_OFF: str
        self.BLINK_OFF: str
        self.REVERSE_OFF: str
        self.HIDE_OFF: str

        self.OFF: str
