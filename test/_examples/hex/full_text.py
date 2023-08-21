# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import bg_hex, hex

if __name__ == "__main__":
    print("")
    hex("I want this text in coral Hex colors", "#ff7f50")
    bg_hex("I want this background in coral Hex colors", "#ff7f50")
    print("")

    hex("I want this text in coral Hex colors", "#ff7f50")
    print("")

    bg_hex("I want this background in coral Hex colors", "#ff7f50")
    print("")
