# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import (BgBrightColor, BgColor, BgColorHex, BgColorHSL,
                      BgColorRGB, BrightColor, Color, ColorHex, ColorHSL,
                      ColorRGB, Effect, green, print_color)

if __name__ == "__main__":
    print("")
    print_color("Normal text without color")
    print_color("Black text", color=Color.BLACK)
    print_color("Bright yellow text", color=BrightColor.YELLOW)
    print_color("RGB color text", color=ColorRGB(127, 57, 203))
    print_color("HSL color text", color=ColorHSL(360, 30, 70))
    print_color("Hex color text", color=ColorHex("#9b9Ac7"))
    print_color("Text on blue background", bg_color=BgColor.BLUE)
    print_color("Text on bright magenta background", bg_color=BgBrightColor.MAGENTA)
    print_color("Text on RGB colored background", bg_color=BgColorRGB(255, 144, 168))
    print_color("Text on HSL colored background", bg_color=BgColorHSL(250, 50, 55))
    print_color("Text on Hex colored background", bg_color=BgColorHex("aB3"))
    print_color("Blinking text", effect=Effect.BLINK)
    print_color("Bold RGB colored text on cyan background", color=ColorRGB(57, 33, 253), bg_color=BgColor.CYAN, effect=Effect.BOLD)
    # Docs homepage:
    print("")
    green("This is GREEN!")
    print("")
    print(f"Both {Color.RED}red{Color.OFF}...")
    print(f"... and {Color.YELLOW}yellow{Color.OFF} are nice colors")
    print("")
