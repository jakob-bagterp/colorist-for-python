# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import colorsys

from ..helper.error import message_for_hex_value_error


def normalize_colorsys_rgb_to_real_rgb(rgb_colorsys: tuple[float, float, float]) -> tuple[int, int, int]:
    """Since Colorsys outputs RGB values as floats between 0.0 an 1.0, we need to normalize this to a standard RGB scale from 0 to 255."""

    red, green, blue = tuple(int(color * 255) for color in rgb_colorsys)
    return red, green, blue


def normalize_hue_degrees_to_colorsys_hue(hue: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare hue between 0 and 360 degrees to a float between 0.0 and 1.0."""

    return hue / 360.0


def normalize_percentage_to_colorsys_value(value: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare lightness, saturation, etc. percentages between 0% and 100% to a float between 0.0 and 1.0."""

    return value / 100.0


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> tuple[int, int, int]:
    hue_colorsys = normalize_hue_degrees_to_colorsys_hue(hue)
    saturation_colorsys = normalize_percentage_to_colorsys_value(saturation)
    lightness_colorsys = normalize_percentage_to_colorsys_value(lightness)
    rgb_colorsys = colorsys.hls_to_rgb(hue_colorsys, lightness_colorsys, saturation_colorsys)
    return normalize_colorsys_rgb_to_real_rgb(rgb_colorsys)


def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    """Convert Hex color to RGB. Expects valid Hex color value with or without hashtag, for instance #B4FBB8 or B4FBB8, #B4F or B4F."""

    hex = hex.lstrip("#")
    if len(hex) == 3:
        red, green, blue = tuple(int(hex[i] * 2, 16) for i in (0, 1, 2))
        return red, green, blue
    elif len(hex) == 6:
        red, green, blue = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        return red, green, blue
    else:
        raise ValueError(message_for_hex_value_error(hex))
