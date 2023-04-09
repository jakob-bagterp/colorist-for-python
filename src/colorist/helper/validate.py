# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

def is_valid_rgb_value(value: int) -> bool:
    return 0 <= value <= 255


def is_valid_hsl_hue(hue: float) -> bool:
    return 0 <= hue <= 360


def is_valid_percentage(value: float) -> bool:
    return 0 <= value <= 100
