# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

def message_for_rgb_value_error(color: str, value: int) -> str:
    return f"Value for \"{color}\" is {value}, but should be integer between 0 and 255."


def message_for_hsl_hue_value_error(value: float) -> str:
    return f"Value for \"hue\" is {value}, but should be number between 0 and 360."


def message_for_hsl_percentage_value_error(param: str, value: float) -> str:
    return f"Value for \"{param}\" is {value}, but should be number between 0(%) and 100(%)."
