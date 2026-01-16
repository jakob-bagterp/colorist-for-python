# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import colorsys
import math

from ..helper.error import message_for_hex_value_error


def colorsys_rgb_to_real_rgb(rgb_colorsys: tuple[float, float, float]) -> tuple[int, int, int]:
    """Since Colorsys outputs RGB values as floats between `0.0` and `1.0`, we need to normalize this to a standard RGB scale from `0` to `255`."""

    red, green, blue = tuple(int(color * 255) for color in rgb_colorsys)
    return red, green, blue


def hue_degrees_to_colorsys_hue(hue: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare hue between `0` and `360` degrees to a decimal between `0.0` and `1.0`."""

    return hue / 360.0


def percentage_to_colorsys_decimal(value: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare lightness, saturation, etc. percentages between `0` and `100` % to a decimal between `0.0` and `1.0`."""

    return value / 100.0


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> tuple[int, int, int]:
    hue_colorsys = hue_degrees_to_colorsys_hue(hue)
    saturation_colorsys = percentage_to_colorsys_decimal(saturation)
    lightness_colorsys = percentage_to_colorsys_decimal(lightness)
    rgb_colorsys = colorsys.hls_to_rgb(hue_colorsys, lightness_colorsys, saturation_colorsys)
    return colorsys_rgb_to_real_rgb(rgb_colorsys)


def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    """Convert Hex color to RGB. Expects valid Hex color value with or without hashtag, for instance `#B4FBB8` or `B4FBB8`, `#B4F` or `B4F`."""

    hex = hex.lstrip("#")
    if len(hex) == 3:
        red, green, blue = tuple(int(hex[i] * 2, 16) for i in (0, 1, 2))
        return red, green, blue
    elif len(hex) == 6:
        red, green, blue = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        return red, green, blue
    else:
        raise ValueError(message_for_hex_value_error(hex))


def oklch_to_oklab(lightness: float, chroma: float, hue: float) -> tuple[float, float, float]:
    hue_radian = math.radians(hue)
    a = chroma * math.cos(hue_radian)
    b = chroma * math.sin(hue_radian)
    return lightness, a, b


def oklab_to_lms(lightness: float, a: float, b: float) -> tuple[float, float, float]:
    long = lightness + 0.3963377774 * a + 0.2158037573 * b
    medium = lightness - 0.1055613458 * a - 0.0638541728 * b
    short = lightness - 0.0894841775 * a - 1.2914855480 * b
    long, medium, short = tuple(color ** 3 for color in (long, medium, short))
    return long, medium, short


def lms_to_linear_rgb(long: float, medium: float, short: float) -> tuple[float, float, float]:
    red = 4.0767416621 * long - 3.3077115913 * medium + 0.2309699292 * short
    green = -1.2684380046 * long + 2.6097574011 * medium - 0.3413193965 * short
    blue = -0.0041960863 * long - 0.7034186147 * medium + 1.7076147010 * short
    return red, green, blue


def gamma_correction_linear_rgb_to_srgb(red: float, green: float, blue: float) -> tuple[int, int, int]:
    def gamma_correction(color: float) -> int:
        if color <= 0:
            return 0
        if color >= 1:
            return 255
        color_corrected = 12.92 * color if color <= 0.0031308 else 1.055 * (color ** (1 / 2.4)) - 0.055
        return int(color_corrected * 255)

    return gamma_correction(red), gamma_correction(green), gamma_correction(blue)


def oklch_to_srgb(lightness: float, chroma: float, hue: float) -> tuple[int, int, int]:
    """Convert OKLCH to RGB. Converts from OKLCH color space (lightness, chroma, hue) to RGB. Expects lightness between `0` and `100`, chroma between `0` and `0.4`, and hue between `0` and `360` degrees."""

    lightness_oklab, a_oklab, b_oklab = oklch_to_oklab(lightness, chroma, hue)
    long_lms, medium_lms, short_lms = oklab_to_lms(lightness_oklab, a_oklab, b_oklab)
    red, green, blue = lms_to_linear_rgb(long_lms, medium_lms, short_lms)
    return gamma_correction_linear_rgb_to_srgb(red, green, blue)
