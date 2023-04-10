# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import BgColor

if __name__ == "__main__":
    print("")
    print(f"I want {BgColor.RED}red{BgColor.OFF} background color inside this paragraph")
    print("")
    print(f"Both {BgColor.GREEN}green{BgColor.OFF} and {BgColor.YELLOW}yellow{BgColor.OFF} are nice background colors")
    print("")
