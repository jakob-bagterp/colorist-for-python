# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import bg_rgb, rgb

if __name__ == "__main__":
    print("")
    rgb("I want this text in blue RGB colors", 0, 128, 255)
    bg_rgb("I want this background in blue RGB colors", 0, 128, 255)
    print("")
