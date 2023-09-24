# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import BgColorHSL, ColorHSL

if __name__ == "__main__":
    mustard_green = ColorHSL(60, 56, 43)
    bg_steel_grey = BgColorHSL(190, 2, 49)

    print("")
    print(f"I want to use {mustard_green}mustard green{mustard_green.OFF} and {bg_steel_grey}steel grey{bg_steel_grey.OFF} colors inside this paragraph")
    print("")

    print("")
    print(f"I want to use {mustard_green}mustard green{mustard_green.OFF} color inside this paragraph")
    print("")

    print("")
    print(f"I want to use {bg_steel_grey}steel grey{bg_steel_grey.OFF} color inside this paragraph")
    print("")
