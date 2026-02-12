# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import colorsys
import math

from ..helper.error import message_for_hex_value_error


def colorsys_rgb_to_real_rgb(rgb_colorsys: tuple[float, float, float]) -> tuple[int, int, int]:
    """Since Colorsys outputs RGB values as floats between `0.0` and `1.0`, we need to normalize this to a standard RGB scale from `0` to `255`.

    Args:
        rgb_colorsys (tuple[float, float, float]): Tuple with RGB colors from Colorsys as floats between `0.0` and `1.0`.

    Returns:
        tuple[int, int, int]: Tuple with RGB colors as integers between `0` and `255`.
    """

    red, green, blue = tuple(int(color * 255) for color in rgb_colorsys)
    return red, green, blue


def hue_degrees_to_colorsys_hue(hue: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare hue between `0` and `360` degrees to a decimal between `0.0` and `1.0`.

    Args:
        hue (float): Number between `0` and `360` degrees.

    Returns:
        float: Decimal between `0.0` and `1.0` for Colorsys.
    """

    return hue / 360.0


def percentage_to_colorsys_decimal(value: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare lightness, saturation, etc. percentages between `0` and `100` % to a decimal between `0.0` and `1.0`.

    Args:
        value (float): Percentage between `0` and `100` %.

    Returns:
        float: Decimal between `0.0` and `1.0` for Colorsys.
    """

    return value / 100.0


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> tuple[int, int, int]:
    """Convert HSL color to RGB.

    Args:
        hue (float): Number between `0` and `360` degrees.
        saturation (float): Percentage between `0` and `100` %.
        lightness (float): Percentage between `0` and `100` %.

    Returns:
        tuple[int, int, int]: Tuple with RGB colors as integers between `0` and `255`.
    """

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
        red, green, blue = tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))
        return red, green, blue
    else:
        raise ValueError(message_for_hex_value_error(hex))


def oklch_to_oklab(lightness: float, chroma: float, hue: float) -> tuple[float, float, float]:
    """Convert OKLCH color space to Oklab.

    Args:
        lightness (float): Lightness value between `0.0` and `1.0` where `0.0` is black and `1.0` is white.
        chroma (float): Chroma value between `0.0` and `0.4`.
        hue (float): Number between `0` and `360` degrees.

    Returns:
        tuple[float, float, float]: Tuple with Oklab values (lightness, a, b).

    References:
        - https://bottosson.github.io/posts/oklab/
        - https://en.wikipedia.org/wiki/Oklab_color_space
    """

    hue_radian = math.radians(hue)
    a = chroma * math.cos(hue_radian)
    b = chroma * math.sin(hue_radian)
    return lightness, a, b


def oklab_to_lms(lightness: float, a: float, b: float) -> tuple[float, float, float]:
    """Convert Oklab color space to LMS cone response.

    Args:
        lightness (float): Lightness value between `0.0` and `1.0` where `0.0` is black and `1.0` is white.
        a (float): Value between `-1.0` and `1.0`.
        b (float): Value between `-1.0` and `1.0`.

    Returns:
        tuple[float, float, float]: Tuple with LMS values (long, medium, short).

    References:
        - https://bottosson.github.io/posts/oklab/
        - https://en.wikipedia.org/wiki/Oklab_color_space
    """

    # Inverse linear map from Oklab to LMS with coefficients from the Oklab specification
    long_prime = lightness + 0.3963377774 * a + 0.2158037573 * b
    medium_prime = lightness - 0.1055613458 * a - 0.0638541728 * b
    short_prime = lightness - 0.0894841775 * a - 1.2914855480 * b

    # Revert the non-linearity (cube root inverse is power of 3)
    long = long_prime**3
    medium = medium_prime**3
    short = short_prime**3

    return long, medium, short


def lms_to_linear_rgb(long: float, medium: float, short: float) -> tuple[float, float, float]:
    """Convert LMS color space to linear RGB.

    Args:
        long (float): Value between `0.0` and `1.0`.
        medium (float): Value between `0.0` and `1.0`.
        short (float): Value between `0.0` and `1.0`.

    Returns:
        tuple[float, float, float]: Tuple with linear RGB values (red, green, blue).

    References:
        - https://en.wikipedia.org/wiki/LMS_color_space
    """

    red = 4.0767416621 * long - 3.3077115913 * medium + 0.2309699292 * short
    green = -1.2684380046 * long + 2.6097574011 * medium - 0.3413193965 * short
    blue = -0.0041960863 * long - 0.7034186147 * medium + 1.7076147010 * short
    return red, green, blue


def gamma_correction_linear_rgb_to_srgb(red: float, green: float, blue: float) -> tuple[int, int, int]:
    """Convert linear RGB color space to sRGB with gamma correction.

    Args:
        red (float): Value between `0.0` and `1.0`.
        green (float): Value between `0.0` and `1.0`.
        blue (float): Value between `0.0` and `1.0`.

    Returns:
        tuple[int, int, int]: Tuple with sRGB values as integers between `0` and `255`.

    References:
        - https://en.wikipedia.org/wiki/SRGB#Transfer_function_(%22gamma%22)
        - http://www.brucelindbloom.com/index.html?Eqn_RGB_to_XYZ.html
    """

    def gamma_correction(color: float) -> int:
        if color <= 0:
            return 0
        if color >= 1:
            return 255
        color_corrected = 12.92 * color if color <= 0.0031308 else 1.055 * (color ** (1 / 2.4)) - 0.055
        return int(color_corrected * 255)

    return gamma_correction(red), gamma_correction(green), gamma_correction(blue)


def oklch_to_srgb(lightness: float, chroma: float, hue: float) -> tuple[int, int, int]:
    """Convert from OKLCH color space to sRGB.

    Args:
        lightness (float): Lightness value between `0.0` and `1.0` where `0.0` is black and `1.0` is white.
        chroma (float): Chroma value between `0.0` and `0.4`.
        hue (float): Number between `0` and `360` degrees.

    Returns:
        tuple[int, int, int]: Tuple with sRGB values as integers between `0` and `255`.
    """

    lightness_oklab, a_oklab, b_oklab = oklch_to_oklab(lightness, chroma, hue)
    long_lms, medium_lms, short_lms = oklab_to_lms(lightness_oklab, a_oklab, b_oklab)
    red, green, blue = lms_to_linear_rgb(long_lms, medium_lms, short_lms)
    return gamma_correction_linear_rgb_to_srgb(red, green, blue)
