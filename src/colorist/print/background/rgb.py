from ... import helper


def bg_rgb(text: str, red: int, green: int, blue: int) -> None:
    """Values for red, green, blue can be between 0 and 255."""

    helper.print.bg_rgb(text, red, green, blue)