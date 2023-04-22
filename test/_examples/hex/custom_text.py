# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import BgColorHex, ColorHex

if __name__ == "__main__":
    watermelon_red = ColorHex("#ff5733")
    bg_mint_green = BgColorHex("#99ff99")

    print("")
    print(f"I want to use {watermelon_red}watermelon pink{watermelon_red.OFF} and {bg_mint_green}mint green{bg_mint_green.OFF} colors inside this paragraph")
    print("")
