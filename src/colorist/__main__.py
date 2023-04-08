from . import helper


def rgb(text: str, red: int, green: int, blue: int) -> None:
    """Values for red, green, blue can be between 0 and 255."""

    helper.print.rgb(text, red, green, blue)


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Values for red, green, blue can be between 0 and 255."""

    helper.print.bg_rgb(text, red, green, blue)


def hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    red, green, blue = helper.convert.hsl_to_rgb(hue, lightness, saturation)
    helper.print.rgb(text, red, green, blue)


def bg_hsl(text: str, hue: float, saturation: float, lightness: float) -> None:
    """Value for hue can be between 0 and 360 degrees, while saturation and lightness can be a percentage between 0(%) and 100(%)."""

    red, green, blue = helper.convert.hsl_to_rgb(hue, lightness, saturation)
    helper.print.bg_rgb(text, red, green, blue)
