# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import BgColorHSL, ColorHSL

if __name__ == "__main__":
    aged_pink = ColorHSL(7, 31, 69)
    bg_steel_gray = BgColorHSL(190, 2, 49)

    print("")
    print(f"I want to use {aged_pink}dusty pink{aged_pink.OFF} and {bg_steel_gray}steel blue{bg_steel_gray.OFF} colors inside this paragraph")
    print("")
