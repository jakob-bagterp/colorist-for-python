from ..constants.ansi import RESET_ALL
from ..model.abc.color import BgColor_ABC, FgColor_ABC
from ..model.abc.effect import Effect_ABC


def color(text: str, color: FgColor_ABC | str = "", bg_color: BgColor_ABC | str = "") -> None:
    print(f"{bg_color}{color}{text}{RESET_ALL}")


def effect(text: str, effect: Effect_ABC | str, color: FgColor_ABC | str = FgColor_ABC.DEFAULT) -> None:
    print(f"{color}{effect}{text}{RESET_ALL}")


def rgb(text: str, red: int, green: int, blue: int) -> None:
    print(f"\033[38;2;{red};{green};{blue}m{text}{RESET_ALL}")


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    print(f"\033[48;2;{red};{green};{blue}m{text}{RESET_ALL}")
