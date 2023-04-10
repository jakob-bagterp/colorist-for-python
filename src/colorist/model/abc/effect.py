# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC


class Effect_ABC(ABC):
    """Abstract base class for standard ANSI color classes."""

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
