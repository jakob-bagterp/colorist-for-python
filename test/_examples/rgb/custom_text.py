# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import BgColorRGB, ColorRGB

if __name__ == "__main__":
    dusty_pink = ColorRGB(194, 145, 164)
    bg_steel_blue = BgColorRGB(70, 130, 180)

    print("")
    print(
        f"I want to use {dusty_pink}dusty pink{dusty_pink.OFF} and {bg_steel_blue}steel blue{bg_steel_blue.OFF} colors inside this paragraph"
    )
    print("")

    print("")
    print(f"I want to use {dusty_pink}dusty pink{dusty_pink.OFF} color inside this paragraph")
    print("")

    print("")
    print(f"I want to use {bg_steel_blue}steel blue{bg_steel_blue.OFF} color inside this paragraph")
    print("")
