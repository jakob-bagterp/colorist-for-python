from ..constants.ansi import RESET_ALL
from ..model.background_bright_color import BgBrightColor
from ..model.background_color import BgColor
from ..model.bright_color import BrightColor
from ..model.color import Color
from ..model.effect import Effect


def color(text: str, color: Color | BrightColor | str = "", bg_color: BgColor | BgBrightColor | str = "") -> None:
    print(f"{bg_color}{color}{text}{RESET_ALL}")


def effect(text: str, effect: Effect | str, color: Color | BrightColor | str = Color.DEFAULT) -> None:
    print(f"{color}{effect}{text}{RESET_ALL}")


def rgb(text: str, red: int, green: int, blue: int) -> None:
    print(f"\033[38;2;{red};{green};{blue}m{text}{RESET_ALL}")


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    print(f"\033[48;2;{red};{green};{blue}m{text}{RESET_ALL}")
