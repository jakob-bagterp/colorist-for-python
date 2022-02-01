from typing import Union
from ..model.background_bright_color import BgBrightColor
from ..model.background_color import BgColor
from ..model.bright_color import BrightColor
from ..model.color import Color
from ..model.effect import Effect

def color(text: str, color: Union[Color, BrightColor, str] = "", bgcolor: Union[BgColor, BgBrightColor, str] = "") -> None:
    print(f"{bgcolor}{color}{text}{Color.OFF}")

def effect(text: str, effect: Effect, color: Union[Color, BrightColor] = Color.DEFAULT) -> None:
    print(f"{color}{effect}{text}{Effect.OFF}")
