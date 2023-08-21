# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from abc import ABC


class MkDocstringsWrapper_ABC(ABC):
    """Abstract base class used to documentation standalone functions now that MkDocstrings (as far as I know) only support reference of functions within classes.

    Should not used for other purposes than documentation."""

    def __init__(self) -> None:
        pass
