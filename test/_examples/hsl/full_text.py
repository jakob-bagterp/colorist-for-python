# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import bg_hsl, hsl

if __name__ == "__main__":
    print("")
    hsl("I want this text in green HSL colors", 120, 50, 50)
    bg_hsl("I want this background in green HSL colors", 120, 50, 50)
    print("")

    hsl("I want this text in green HSL colors", 120, 50, 50)
    print("")

    bg_hsl("I want this background in green HSL colors", 120, 50, 50)
    print("")
