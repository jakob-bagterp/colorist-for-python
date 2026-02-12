# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import BgColorHex, ColorHex

if __name__ == "__main__":
    watermelon_red = ColorHex("#ff5733")
    bg_mint_green = BgColorHex("#99ff99")

    print("")
    print(
        f"I want to use {watermelon_red}watermelon red{watermelon_red.OFF} and {bg_mint_green}mint green{bg_mint_green.OFF} colors inside this paragraph"
    )
    print("")

    print("")
    print(f"I want to use {watermelon_red}watermelon red{watermelon_red.OFF} color inside this paragraph")
    print("")

    print("")
    print(f"I want to use {bg_mint_green}mint green{bg_mint_green.OFF} color inside this paragraph")
    print("")
