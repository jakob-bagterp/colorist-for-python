# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from collections.abc import Callable

from colorist.model.abc.color import BgColor_ABC, FgColor_ABC

PrintFullTextCallable = Callable[[str], None]

PrintEffectCallable = Callable[[str], None]

PrintEffectWithColorCallable = Callable[[str, FgColor_ABC | BgColor_ABC], None]
