# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

import colorsys


def normalise_colorsys_rgb_to_real_rgb(rgb_colorsys: tuple[float, float, float]) -> tuple[int, int, int]:
    """Since Colorsys outputs RGB values as floats between 0.0 an 1.0, we need to normalise this to a standard RGB scale from 0 to 255."""

    red, green, blue = tuple(int(color * 255) for color in rgb_colorsys)
    return red, green, blue


def normalise_hue_degrees_to_colorsys_hue(hue: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare hue between 0 and 360 degrees to a float between 0.0 and 1.0."""

    return hue / 360.0


def normalise_percentage_to_colorsys_value(value: float) -> float:
    """When converting HLS or HSV with Colorsys, we need to prepare lightness, saturation, etc. percentages between 0% and 100% to a float between 0.0 and 1.0."""

    return value / 100.0


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> tuple[int, int, int]:
    hue_colorsys = normalise_hue_degrees_to_colorsys_hue(hue)
    saturation_colorsys = normalise_percentage_to_colorsys_value(saturation)
    lightness_colorsys = normalise_percentage_to_colorsys_value(lightness)
    rgb_colorsys = colorsys.hls_to_rgb(hue_colorsys, lightness_colorsys, saturation_colorsys)
    return normalise_colorsys_rgb_to_real_rgb(rgb_colorsys)
