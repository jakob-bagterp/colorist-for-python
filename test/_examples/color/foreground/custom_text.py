# Copyright 2022 – present, Jakob Bagterp. BSD 3-Clause license and refer to LICENSE file.

from colorist import Color

if __name__ == "__main__":
    print("")
    print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
    print("")
    print(f"Both {Color.GREEN}green{Color.OFF} and {Color.YELLOW}yellow{Color.OFF} are nice colors")
    print("")
    print(f"I want {Color.RED}red{Color.OFF} color inside this paragraph")
    print("")
    print("I want " + Color.RED + "red" + Color.OFF + " color inside this paragraph")
    print("")
