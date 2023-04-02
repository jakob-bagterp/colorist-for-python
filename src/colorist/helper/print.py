from ..model.background_bright_color import BgBrightColor
from ..model.background_color import BgColor
from ..model.bright_color import BrightColor
from ..model.color import Color
from ..model.effect import Effect


def color(text: str, color: Color | BrightColor | str = "", bgcolor: BgColor | BgBrightColor | str = "") -> None:
    print(f"{bgcolor}{color}{text}{Color.OFF}")


def effect(text: str, effect: Effect | str, color: Color | BrightColor | str = Color.DEFAULT) -> None:
    print(f"{color}{effect}{text}{Effect.OFF}")


def rgb(text: str, red: int, green: int, blue: int) -> None:
    print(f"\033[38;2;{red};{green};{blue}m{text}{Color.OFF}")


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    print(f"\033[48;2;{red};{green};{blue}m{text}{Color.OFF}")
